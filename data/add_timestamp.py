import pandas as pd
import random
from datetime import datetime, timedelta

# Load existing data
df = pd.read_csv("data/student_satisfaction.csv")

# Generate random timestamps (last 60 days)
start_date = datetime.now() - timedelta(days=60)

timestamps = []

for _ in range(len(df)):
    random_days = random.randint(0, 60)
    random_time = start_date + timedelta(days=random_days)
    timestamps.append(random_time)

# Add column
df["timestamp"] = timestamps

# Save updated file
df.to_csv("data/student_satisfaction.csv", index=False)

print("Timestamp column added successfully!")