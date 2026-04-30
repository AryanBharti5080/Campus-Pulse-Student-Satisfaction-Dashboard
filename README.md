# 🎓 Campus Pulse Student Satisfaction Dashboard

A full-stack data analytics dashboard that visualizes student satisfaction across campus facilities like Library, Cafeteria, Hostel, Sports Center, and WiFi.

This project demonstrates end-to-end development including data generation, analysis, backend APIs, and an interactive frontend dashboard.

---

## 🚀 Project Overview

Campus Pulse helps analyze how students feel about different campus facilities.

It allows users to:
- View overall satisfaction metrics
- Analyze trends across departments and years
- Filter data dynamically
- Visualize insights using charts

---

## 🛠️ Tech Stack

**Frontend**
- HTML
- CSS
- JavaScript
- Chart.js

**Backend**
- Python
- FastAPI

**Data Processing**
- Pandas

---

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


---

## 📊 Features

### 🔹 Dashboard Metrics
- Total Responses
- Average Satisfaction Score
- Best Performing Facility

### 🔹 Interactive Charts
- Average Score by Facility (Bar Chart)
- Responses Distribution (Pie Chart)
- Department-wise Analysis
- Year-wise Trends (Line Chart)

### 🔹 Filters
- Facility
- Department
- Year

### 🔹 Authentication
- Admin login system
- Session handled using localStorage

---

## 🔐 Login Credentials
Username: admin
Password: admin123

## ⚙️ Setup Instructions (Windows)

### 1. Clone Repository

git clone https://github.com/your-username/Campus_Pulse_Dashboard.git

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

---

## 📡 API Endpoints

| Endpoint     | Method | Description |
|-------------|--------|------------|
| `/data`      | GET    | Returns full dataset |
| `/metrics`   | GET    | Returns summary metrics |
| `/filtered`  | GET    | Returns filtered data |
| `/login`     | POST   | Admin login |

---

## 📈 Sample Use Cases

- Identify which facility needs improvement  
- Compare satisfaction across departments  
- Analyze trends across academic years  
- Build data-driven campus decisions  

---

## 💡 Learning Outcomes

This project demonstrates:

- Full-stack development using FastAPI and JavaScript  
- Data analysis using Pandas  
- API creation and consumption  
- Interactive dashboard design  
- Real-world project structuring  

---

## 🔮 Future Enhancements

- Role-based authentication  
- Database integration (MySQL / PostgreSQL)  
- Deployment on cloud (AWS / Render)  
- Advanced analytics (ML predictions)  
- Export reports (PDF/Excel)  

---

## 👨‍💻 Author

**Aryan Bharti**

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub and share your feedback!
