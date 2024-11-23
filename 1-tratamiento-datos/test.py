#EJEMPLO BÁSICO
import findspark
from pyspark.sql import SparkSession

findspark.init()

# Crear una sesión de Spark
spark = SparkSession.builder \
    .appName("Basic Example") \
    .getOrCreate()

# Crear un DataFrame simple
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
columns = ["Name", "Id"]

df = spark.createDataFrame(data, columns)

# Mostrar el DataFrame
df.show()

# Detener la sesión de Spark
spark.stop()
