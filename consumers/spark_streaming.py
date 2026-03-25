from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("StreamingAnalytics") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

schema = StructType([
    StructField("event_id", StringType()),
    StructField("user_id", StringType()),
    StructField("event_type", StringType()),
    StructField("timestamp", StringType()),
    StructField("page", StringType()),
    StructField("amount", DoubleType()),
    StructField("session_id", StringType()),
    StructField("device", StringType())
])

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "streaming-data") \
    .option("startingOffsets", "latest") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)")

data = json_df.select(
    from_json(col("value"), schema).alias("data")
).select("data.*")

data = data.withColumn(
    "timestamp",
    to_timestamp("timestamp")
)

agg = data.groupBy(
    window(col("timestamp"), "1 minute")
).agg(
    count("*").alias("events_per_minute"),
    sum("amount").alias("revenue")
)

query = agg.writeStream \
    .outputMode("update") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()