from pyspark.sql.functions import *

def compute_metrics(df):
    return df.groupBy("event_type").agg(
        count("*").alias("count"),
        avg("amount").alias("avg_amount")
    )