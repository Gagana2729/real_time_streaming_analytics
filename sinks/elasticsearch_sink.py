def write_elastic(df):
    return df.writeStream \
        .format("org.elasticsearch.spark.sql") \
        .option("checkpointLocation", "checkpoints/es") \
        .start("streaming/events")