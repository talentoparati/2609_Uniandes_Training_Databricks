# Databricks notebook source
# MAGIC %md
# MAGIC <div style="box-sizing:border-box;width:100%;background:linear-gradient(135deg,#0a2a6e 0%,#0d5c8a 45%,#0d9488 100%);padding:22px 18px 18px 18px;border-radius:12px 12px 0 0;">
# MAGIC   <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
# MAGIC     <div style="flex:1;min-width:0;">
# MAGIC       <span style="background:rgba(255,255,255,0.18);color:#a8f0e0;font-size:10px;letter-spacing:2px;padding:3px 10px;border-radius:20px;font-weight:600;">DATABRICKS &nbsp;&middot;&nbsp; SETUP</span>
# MAGIC       <h1 style="color:#ffffff;font-size:21px;margin:10px 0 4px 0;font-weight:700;">Configuracion Central del Curso</h1>
# MAGIC       <p style="color:#b2f0e8;font-size:13px;margin:0;">Widgets + parametros compartidos por todos los notebooks</p>
# MAGIC     </div>
# MAGIC     <div style="text-align:right;flex-shrink:0;">
# MAGIC       <div style="color:#ffffff;font-size:15px;font-weight:800;">Uniandes</div>
# MAGIC       <div style="color:#7de8d8;font-size:10px;margin-top:2px;">Educacion Continua &middot; Databricks 2026</div>
# MAGIC     </div>
# MAGIC   </div>
# MAGIC </div>
# MAGIC <div style="box-sizing:border-box;width:100%;background:#0f172a;padding:12px 18px;border-radius:0 0 12px 12px;margin-bottom:6px;">
# MAGIC   <table style="width:100%;border-collapse:collapse;table-layout:fixed;">
# MAGIC     <tr>
# MAGIC       <td style="width:50%;padding:8px 10px 8px 0;border-right:1px solid #1e3a5f;vertical-align:top;">
# MAGIC         <div style="color:#64748b;font-size:10px;letter-spacing:1px;margin-bottom:3px;">PROPOSITO</div>
# MAGIC         <div style="color:#e2e8f0;font-size:12px;">Unico lugar donde viven los widgets y parametros del entorno. Ningun otro notebook del curso define un widget propio.</div>
# MAGIC       </td>
# MAGIC       <td style="width:50%;padding:8px 0 8px 10px;vertical-align:top;">
# MAGIC         <div style="color:#64748b;font-size:10px;letter-spacing:1px;margin-bottom:3px;">USO</div>
# MAGIC         <div style="color:#e2e8f0;font-size:12px;">Cada notebook de sesion empieza con <code>%run ../00_Setup/00_Configuracion</code> para heredar estas variables.</div>
# MAGIC       </td>
# MAGIC     </tr>
# MAGIC   </table>
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC <div style="box-sizing:border-box;width:100%;background:#0c1a2e;border:1px solid #1e3a5f;border-left:4px solid #0d9488;border-radius:6px;margin:10px 0;overflow:hidden;">
# MAGIC   <div style="padding:8px 16px;border-bottom:1px solid #1e3a5f;background:rgba(13,148,136,0.08);">
# MAGIC     <span style="color:#2dd4bf;font-size:10px;font-weight:700;letter-spacing:1.5px;">COMPATIBILIDAD — DATABRICKS FREE EDITION</span>
# MAGIC   </div>
# MAGIC   <div style="padding:10px 16px;color:#cbd5e1;font-size:13px;">Este curso corre 100% en Databricks Free Edition: Compute Serverless (sin clusters clasicos), Unity Catalog habilitado por defecto, 1 SQL Warehouse 2X-Small y Jobs con hasta 5 tasks concurrentes por cuenta. Ninguna celda del curso requiere una feature exclusiva de un plan pago.</div>
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC <div style="box-sizing:border-box;width:100%;background:#0c1a2e;border:1px solid #1e3a5f;border-left:4px solid #2563eb;border-radius:6px;margin:10px 0;overflow:hidden;">
# MAGIC   <div style="padding:8px 16px;border-bottom:1px solid #1e3a5f;background:rgba(37,99,235,0.08);">
# MAGIC     <span style="color:#38bdf8;font-size:10px;font-weight:700;letter-spacing:1.5px;">ANTES DE EJECUTAR ESTA CELDA</span>
# MAGIC   </div>
# MAGIC   <table style="width:100%;border-collapse:collapse;">
# MAGIC     <tr>
# MAGIC       <td style="width:78px;padding:8px 4px 6px 16px;vertical-align:top;color:#64748b;font-size:10px;letter-spacing:1px;white-space:nowrap;">QUE HACE</td>
# MAGIC       <td style="padding:8px 16px 6px 0;color:#e2e8f0;font-size:13px;">Declara 6 <code style="color:#38bdf8;">dbutils.widgets</code> en la barra superior del notebook: catalog, entorno y los 3 tamanos del dataset sintetico.</td>
# MAGIC     </tr>
# MAGIC     <tr>
# MAGIC       <td style="padding:6px 4px 6px 16px;vertical-align:top;color:#64748b;font-size:10px;letter-spacing:1px;white-space:nowrap;">PARA QUE</td>
# MAGIC       <td style="padding:6px 16px 6px 0;color:#93c5fd;font-size:13px;">Para poder cambiar catalog o tamano de datos <strong style="color:#e2e8f0;">sin editar codigo</strong> — el instructor o un Job pueden inyectar un valor distinto. Se centralizan aqui <u>todos</u> los widgets del curso: ningun notebook de sesion vuelve a declarar un <code style="color:#38bdf8;">dbutils.widgets</code> propio, para que los 16 notebooks nunca queden desincronizados.</td>
# MAGIC     </tr>
# MAGIC     <tr>
# MAGIC       <td style="padding:6px 4px 10px 16px;vertical-align:top;color:#64748b;font-size:10px;letter-spacing:1px;white-space:nowrap;">COMO LO HACE</td>
# MAGIC       <td style="padding:6px 16px 10px 0;color:#93c5fd;font-size:13px;"><code style="color:#38bdf8;">dbutils.widgets.text(nombre, valor_por_defecto, etiqueta)</code> crea un campo de texto libre; <code style="color:#38bdf8;">dropdown(nombre, valor_por_defecto, opciones, etiqueta)</code> crea una lista desplegable. Ambos persisten su valor mientras el notebook este adjunto al compute — no hace falta volver a escribirlos al re-ejecutar. Referencia oficial: <a href="https://docs.databricks.com/aws/en/notebooks/widgets" style="color:#38bdf8;">docs.databricks.com/notebooks/widgets</a>.</td>
# MAGIC     </tr>
# MAGIC   </table>
# MAGIC </div>

# COMMAND ----------

# ============================================================
# WIDGETS DEL CURSO — unico lugar donde se declaran
# Todos los notebooks de sesion heredan estos valores via %run
# ============================================================

dbutils.widgets.text("catalog_name", "ecommerce_training", "01 · Catalog (Unity Catalog)")
dbutils.widgets.dropdown("entorno", "training", ["training", "dev", "demo"], "02 · Entorno")
dbutils.widgets.text("num_clientes", "8000", "03 · Clientes sinteticos")
dbutils.widgets.text("num_sesiones", "40000", "04 · Sesiones web sinteticas")
dbutils.widgets.text("num_transacciones", "20000", "05 · Transacciones sinteticas")
dbutils.widgets.text("semilla_random", "2609", "06 · Semilla aleatoria")

# COMMAND ----------

# MAGIC %md
# MAGIC <div style="box-sizing:border-box;width:100%;background:#0c1a2e;border:1px solid #1e3a5f;border-left:4px solid #2563eb;border-radius:6px;margin:10px 0;overflow:hidden;">
# MAGIC   <div style="padding:8px 16px;border-bottom:1px solid #1e3a5f;background:rgba(37,99,235,0.08);">
# MAGIC     <span style="color:#38bdf8;font-size:10px;font-weight:700;letter-spacing:1.5px;">ANTES DE EJECUTAR ESTA CELDA</span>
# MAGIC   </div>
# MAGIC   <table style="width:100%;border-collapse:collapse;">
# MAGIC     <tr>
# MAGIC       <td style="width:78px;padding:8px 4px 6px 16px;vertical-align:top;color:#64748b;font-size:10px;letter-spacing:1px;white-space:nowrap;">QUE HACE</td>
# MAGIC       <td style="padding:8px 16px 6px 0;color:#e2e8f0;font-size:13px;">Lee los 6 widgets con <code style="color:#38bdf8;">dbutils.widgets.get()</code> y los vuelca en variables Python en MAYUSCULAS; agrega los 3 nombres de schema fijos y una funcion helper <code style="color:#38bdf8;">tbl()</code>.</td>
# MAGIC     </tr>
# MAGIC     <tr>
# MAGIC       <td style="padding:6px 4px 6px 16px;vertical-align:top;color:#64748b;font-size:10px;letter-spacing:1px;white-space:nowrap;">PARA QUE</td>
# MAGIC       <td style="padding:6px 16px 6px 0;color:#93c5fd;font-size:13px;">Los widgets viven en la UI del notebook; el resto del codigo del curso necesita <strong style="color:#e2e8f0;">variables Python normales</strong> para usarlas dentro de f-strings y llamadas de PySpark. <code style="color:#38bdf8;">bronze</code>/<code style="color:#38bdf8;">silver</code>/<code style="color:#38bdf8;">gold</code> no son widgets porque son un estandar fijo de la Arquitectura Medallion — no tiene sentido parametrizarlos.</td>
# MAGIC     </tr>
# MAGIC     <tr>
# MAGIC       <td style="padding:6px 4px 10px 16px;vertical-align:top;color:#64748b;font-size:10px;letter-spacing:1px;white-space:nowrap;">COMO LO HACE</td>
# MAGIC       <td style="padding:6px 16px 10px 0;color:#93c5fd;font-size:13px;">Mismo patron que usan los <a href="https://github.com/databricks-demos/dbdemos" style="color:#38bdf8;">dbdemos oficiales de Databricks</a>: variables en MAYUSCULAS, asignadas una sola vez, usadas por lectura en todo el codigo posterior. <code style="color:#38bdf8;">tbl(schema, tabla)</code> concatena <code style="color:#38bdf8;">catalog.schema.tabla</code> para no repetir ese f-string en cada notebook.</td>
# MAGIC     </tr>
# MAGIC   </table>
# MAGIC </div>

# COMMAND ----------

CATALOG_NAME = dbutils.widgets.get("catalog_name")
ENTORNO = dbutils.widgets.get("entorno")
NUM_CLIENTES = int(dbutils.widgets.get("num_clientes"))
NUM_SESIONES = int(dbutils.widgets.get("num_sesiones"))
NUM_TRANSACCIONES = int(dbutils.widgets.get("num_transacciones"))
SEED = int(dbutils.widgets.get("semilla_random"))

# Arquitectura Medallion — estandar fijo, no parametrizable
SCHEMA_BRONZE = "bronze"
SCHEMA_SILVER = "silver"
SCHEMA_GOLD = "gold"

# Volumen para Auto Loader / landing zone incremental (Modulo 3 y 5)
VOLUME_LANDING = "landing"


def tbl(schema, tabla):
    """Nombre completo catalog.schema.tabla — usar SIEMPRE esta funcion en vez de hardcodear."""
    return f"{CATALOG_NAME}.{schema}.{tabla}"


print("=" * 60)
print("CONFIGURACION CARGADA")
print("=" * 60)
print(f"  catalog_name       = {CATALOG_NAME}")
print(f"  entorno            = {ENTORNO}")
print(f"  num_clientes       = {NUM_CLIENTES:,}")
print(f"  num_sesiones       = {NUM_SESIONES:,}")
print(f"  num_transacciones  = {NUM_TRANSACCIONES:,}")
print(f"  semilla_random     = {SEED}")
print(f"  schemas medallion  = {SCHEMA_BRONZE}, {SCHEMA_SILVER}, {SCHEMA_GOLD}")

# COMMAND ----------

# MAGIC %md
# MAGIC <div style="box-sizing:border-box;width:100%;background:linear-gradient(90deg,#0a2a6e,#0d9488);height:3px;border-radius:2px;margin:20px 0 8px 0;"></div>
# MAGIC <div style="box-sizing:border-box;width:100%;display:flex;justify-content:space-between;color:#64748b;font-size:12px;">
# MAGIC   <span>Setup &middot; Configuracion &middot; Siguiente: <strong>01_Generacion_Datos_Sinteticos</strong></span>
# MAGIC </div>
