from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi import HTTPException

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load dataset
df = pd.read_csv("data/student_satisfaction.csv")

# Home route (test)
@app.get("/")
def home():
    return {"message": "Campus Pulse Student Satisfaction Dashboard's Backend (Running)"}

# Get all data
@app.get("/data")
def get_data():
    return df.to_dict(orient="records")
#Calculate Insights
@app.get("/metrics")
def get_metrics():
    total_responses = len(df)
    average_score = df["satisfaction_score"].mean()

    # Average score by facility
    facility_avg = df.groupby("facility")["satisfaction_score"].mean()

    # Best facility (highest average score)
    best_facility = facility_avg.idxmax()

    return {
        "total_responses": total_responses,
        "average_score": round(average_score, 2),
        "best_facility": best_facility
    }

#Dynamic Filtering
@app.get("/filtered")
def get_filtered_data(
    facility: str = None,
    department: str = None,
    year: str = None
):
    filtered_df = df.copy()

    # Apply filters only if values are provided
    if facility:
        filtered_df = filtered_df[filtered_df["facility"] == facility]

    if department:
        filtered_df = filtered_df[filtered_df["department"] == department]

    if year:
        filtered_df = filtered_df[filtered_df["year"] == year]

    return filtered_df.to_dict(orient="records")

#LOGIN as ADmin Only
@app.post("/login")
def login(username: str, password: str):
    
    # Hardcoded admin credentials (simple for beginners)
    if username == "admin" and password == "admin123":
        return {"message": "Login successful"}
    
    raise HTTPException(status_code=401, detail="Invalid username or password")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)