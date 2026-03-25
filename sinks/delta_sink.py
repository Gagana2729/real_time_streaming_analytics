def write_delta(df):
    return df.writeStream \
        .format("delta") \
        .option("checkpointLocation", "checkpoints/delta") \
        .start("data/delta")