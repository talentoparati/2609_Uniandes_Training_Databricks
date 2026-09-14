# Databricks notebook source
# MAGIC %md
# MAGIC # Pipeline Declarativo Completo — Bronze -> Silver -> Gold
# MAGIC
# MAGIC Este archivo NO se ejecuta con %run. Se registra como codigo fuente de un recurso
# MAGIC **Lakeflow Declarative Pipeline** (Workflows > Lakeflow Declarative Pipelines > Create Pipeline).
# MAGIC Extiende el pipeline del Modulo 3 (Sesion 8) hasta la capa Gold — en Databricks Free Edition
# MAGIC (limite de 1 pipeline activo por tipo) esto significa actualizar el MISMO recurso, no crear uno nuevo.
# MAGIC Ver Modulo 5 / Sesion 12 para el equivalente materializado en batch.

# COMMAND ----------

from pyspark import pipelines as dp
from pyspark.sql import functions as F
from pyspark.sql.functions import broadcast

CATALOG_NAME = spark.conf.get("pipelines.catalog", "ecommerce_training")
LANDING_PATH = f"/Volumes/{CATALOG_NAME}/bronze/landing/eventos_carrito"

# COMMAND ----------

# MAGIC %md ## Bronze — ingesta incremental con Auto Loader

# COMMAND ----------

@dp.table(name="eventos_carrito_bronze", comment="Ingesta incremental via Auto Loader")
def eventos_carrito_bronze():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load(LANDING_PATH)
        .withColumn("_ingested_at", F.current_timestamp())
    )

# COMMAND ----------

# MAGIC %md ## Silver — calidad de datos declarativa

# COMMAND ----------

@dp.table(name="eventos_carrito_silver", comment="Eventos limpios y validados")
@dp.expect_or_drop("cantidad_valida", "cantidad > 0")
@dp.expect_or_drop("precio_valido", "precio_unitario > 0")
def eventos_carrito_silver():
    return dp.read_stream("eventos_carrito_bronze").dropDuplicates(["evento_id"])

# COMMAND ----------

# MAGIC %md ## Gold — metricas de negocio listas para BI y ML

# COMMAND ----------

@dp.table(name="resumen_embudo_streaming", comment="Embudo de conversion calculado sobre la ingesta incremental")
def resumen_embudo_streaming():
    return (
        dp.read("eventos_carrito_silver")
        .groupBy("tipo_evento")
        .agg(F.countDistinct("sesion_id").alias("sesiones"))
    )
