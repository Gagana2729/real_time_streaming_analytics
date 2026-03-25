import streamlit as st
import pandas as pd
import time
import random

st.title("Real-Time Streaming Dashboard")

placeholder = st.empty()

while True:
    data = {
        "events_per_sec": random.randint(100, 500),
        "revenue": random.randint(1000, 5000),
        "active_users": random.randint(50, 200)
    }

    df = pd.DataFrame([data])

    placeholder.table(df)

    time.sleep(2)