from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType, FloatType

# Create Spark session with PostgreSQL and Kafka jars
spark = SparkSession.builder \
    .appName("RetailSalesStream") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0") \
    .config("spark.jars", "/Users/ajithkumardugyala/Downloads/jars/postgresql-42.2.27.jar") \
    .getOrCreate()

# Define schema of JSON in Kafka
schema = StructType() \
    .add("store_id", IntegerType()) \
    .add("timestamp", StringType()) \
    .add("item", StringType()) \
    .add("category", StringType()) \
    .add("quantity", IntegerType()) \
    .add("price", FloatType())

# Read from Kafka topic
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "retail_sales") \
    .load()

# Parse the JSON value from Kafka
json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Write to PostgreSQL using foreachBatch
query = json_df.writeStream \
    .outputMode("append") \
    .foreachBatch(lambda batch_df, epoch_id: batch_df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/retail_db") \
        .option("dbtable", "retail_sales_stream") \
        .option("user", "ajithkumardugyala") \
        .option("password", "Ajith@2001") \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()) \
    .start()

query.awaitTermination()
