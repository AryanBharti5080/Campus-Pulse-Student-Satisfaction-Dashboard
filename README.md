# 🎓 Campus Pulse Student Satisfaction Dashboard

A full-stack data analytics dashboard that visualizes student satisfaction across campus facilities like Library, Cafeteria, Hostel, Sports Center, and WiFi.

This project demonstrates end-to-end development including data generation, analysis, backend APIs, and an interactive frontend dashboard.


## 🚀 Project Overview

Campus Pulse helps analyze how students feel about different campus facilities.

It allows Admin to:
1. View overall satisfaction metrics.
2. Analyze trends across departments and years
3. Filter data dynamically 
4. Visualize insights using charts


## 🛠️ Tech Stack

**Frontend**
1. HTML
2. CSS
3. JavaScript
4. Chart.js

**Backend**
1. Python
2. FastAPI

**Data Processing**
1. Pandas



## 📂 Project Structure


Campus_Pulse_Dashboard/
│
├── backend/
│ └── app.py
│
├── data/
│ ├── generate_data.py
│ └── student_satisfaction.csv
│
├── frontend/
│ ├── index.html
│ └── login.html
│
├── notebooks/
│ └── eda.py
│
├── venv/
└── README.md




## 📊 Features

### 🔹 Dashboard Metrics
1.Total Responses
2. Average Satisfaction Score
3. Best Performing Facility

### 🔹 Interactive Charts
1. Average Score by Facility (Bar Chart)
2. Responses Distribution (Pie Chart)
3. Department-wise Analysis
4. Year-wise Trends (Line Chart)

### 🔹 Filters
1. Facility
2. Department
3. Year

### 🔹 Authentication
1. Admin login system
2. Session handled using localStorage


## 🔐 Login Credentials
Username: admin
Password: admin123

## ⚙️ Setup Instructions (Windows)

### 1. Clone Repository

git clone https://github.com/AryanBharti5080/Campus-Pulse-Student-Satisfaction-Dashboard.git

cd Campus_Pulse_Dashboard


### 2. Create Virtual Environment


python -m venv venv
venv\Scripts\activate


### 3. Install Dependencies


pip install pandas matplotlib fastapi uvicorn


### 4. Generate Dataset


python data/generate_data.py



### 5. Run Backend Server


uvicorn backend.app:app --reload


Open:

http://127.0.0.1:8000/docs



### 6. Run Frontend

Open:

frontend/index.html


in your browser.



## 📡 API Endpoints

| Endpoint     | Method | Description |
|-------------|--------|------------|
| `/data`      | GET    | Returns full dataset |
| `/metrics`   | GET    | Returns summary metrics |
| `/filtered`  | GET    | Returns filtered data |
| `/login`     | POST   | Admin login |



## 📈 Sample Use Cases

1. Identify which facility needs improvement  
2. Compare satisfaction across departments  
3. Analyze trends across academic years  
4. Build data-driven campus decisions  



## 💡 Learning Outcomes

This project demonstrates:

1. Perform basic data acquisition, cleaning, and exploratory data analysis.
2. Use a programming language (Python) and relevant libraries (pandas, Matplotlib) to analyze data.
3. Develop a basic web application to present data insights. Understand the interplay between a
   backend data processing service and a frontend user interface.
4. Full-stack development using FastAPI and JavaScript  
5. Data analysis using Pandas  
6. API creation and consumption  
7. Interactive dashboard design  
8. Real-world project structuring  

-

## 🔮 Future Enhancements

1. Role-based authentication  
2. Database integration (MySQL / PostgreSQL)  
3. Deployment on cloud (AWS / Render)  
4. Advanced analytics (ML predictions)  
5. Export reports (PDF/Excel)  



## 👨‍💻 Author

**Aryan Bharti**

#  Demo Video Link:
##  https://drive.google.com/file/d/1hcjo1N8PgzSsSBAhuN6fyy4P3MIsyOzl/view?usp=drive_link





## ⭐ If You Like This Project

Give it a ⭐ on GitHub and share your feedback!
