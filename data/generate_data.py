import pandas as pd
import random

# Number of records
num_records = 800

# Possible values
genders = ["Male", "Female"]
years = ["1st Year", "2nd Year", "3rd Year", "4th Year"]
departments = ["Engineering", "Management", "Science", "Arts"]
facilities = ["Library", "Cafeteria", "Sports Center", "Hostel", "WiFi"]

data = []

for i in range(num_records):
    record = {
        "student_id": i + 1,
        "gender": random.choice(genders),
        "year": random.choice(years),
        "department": random.choice(departments),
        "facility": random.choice(facilities),
        "satisfaction_score": random.randint(1, 5)  # Rating 1 to 5
    }
    data.append(record)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/student_satisfaction.csv", index=False)

print("Dataset created successfully!")