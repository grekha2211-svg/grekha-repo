# Create a DataFrame and add new columns in PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when, upper

spark = SparkSession.builder.appName("DataFrameExample").master("local[*]").getOrCreate()

# Create DataFrame
data = [("Rekha", 25, 50000),
        ("Arun", 30, 65000),
        ("Meena", 28, 58000)]
columns = ["name", "age", "salary"]
df = spark.createDataFrame(data, columns)
print("Original DataFrame:")
df.show()

# New column with a constant value
df = df.withColumn("country", lit("India"))

# New column from calculation
df = df.withColumn("bonus", col("salary") * 0.10)

# New column with condition
df = df.withColumn("level", when(col("age") >= 30, "Senior").otherwise("Junior"))

# New column by transforming existing one
df = df.withColumn("name_upper", upper(col("name")))

print("DataFrame with new columns:")
df.show()

spark.stop()
