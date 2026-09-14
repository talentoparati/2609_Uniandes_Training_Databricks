# Databricks notebook source
# MAGIC %md
# MAGIC # Pipeline Declarativo — Bronze -> Silver (eventos_carrito)
# MAGIC
# MAGIC Este archivo NO se ejecuta con %run. Se registra como codigo fuente de un recurso
# MAGIC **Lakeflow Declarative Pipeline** (Workflows > Lakeflow Declarative Pipelines > Create Pipeline).
# MAGIC Disponible en Databricks Free Edition con el limite de 1 pipeline activo por tipo —
# MAGIC este mismo pipeline se EXTIENDE (no se duplica) hasta Gold en el Modulo 5 / Sesion 12.
# MAGIC
# MAGIC Sintaxis: `from pyspark import pipelines as dp` es la forma recomendada actual
# MAGIC (el modulo histórico `dlt` con `@dlt.table` sigue funcionando como alias, pero
# MAGIC ya no es la forma recomendada para código nuevo).

# COMMAND ----------

from pyspark import pipelines as dp
from pyspark.sql import functions as F

CATALOG_NAME = spark.conf.get("pipelines.catalog", "ecommerce_training")
LANDING_PATH = f"/Volumes/{CATALOG_NAME}/bronze/landing/eventos_carrito"

# COMMAND ----------

# MAGIC %md
# MAGIC ## Capa Bronze — ingesta declarativa con Auto Loader
# MAGIC
# MAGIC `@dp.table` declara QUE tabla existe. Lakeflow decide COMO y CUANDO ejecutarla
# MAGIC segun el grafo de dependencias que se infiere de las funciones `dp.read()` usadas mas abajo.

# COMMAND ----------

@dp.table(
    name="eventos_carrito_bronze",
    comment="Ingesta incremental de eventos de carrito via Auto Loader (Lakeflow Declarative Pipelines)",
)
def eventos_carrito_bronze():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load(LANDING_PATH)
        .withColumn("_ingested_at", F.current_timestamp())
    )

# COMMAND ----------

# MAGIC %md
# MAGIC ## Capa Silver — calidad de datos declarativa con expectativas
# MAGIC
# MAGIC `@dp.expect_or_drop` es el equivalente declarativo a los filtros de calidad que se
# MAGIC escribieron a mano en el Modulo 2 (Tema 2.2) — la diferencia es que Lakeflow reporta
# MAGIC automaticamente cuantos registros violaron cada regla, sin codigo adicional.

# COMMAND ----------

@dp.table(
    name="eventos_carrito_silver",
    comment="Eventos de carrito limpios y validados — capa Silver declarativa",
)
@dp.expect_or_drop("cantidad_valida", "cantidad > 0")
@dp.expect_or_drop("precio_valido", "precio_unitario > 0")
@dp.expect("tipo_evento_conocido", "tipo_evento IN ('view_product','add_to_cart','remove_from_cart','begin_checkout','purchase')")
def eventos_carrito_silver():
    return dp.read_stream("eventos_carrito_bronze").dropDuplicates(["evento_id"])
