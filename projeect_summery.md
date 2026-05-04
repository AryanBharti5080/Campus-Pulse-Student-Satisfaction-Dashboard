# Campus Pulse Dashboard - Project Summary

## Project Name

Campus Pulse Student Satisfaction Dashboard

## Project Overview

Campus Pulse Dashboard is a full-stack data analytics web application that helps visualize student satisfaction across different campus facilities. The project uses generated student feedback data, a FastAPI backend, and an interactive frontend dashboard built with HTML, CSS, JavaScript, and Chart.js.

The dashboard allows an admin user to view overall satisfaction metrics, compare facilities, analyze department-wise and year-wise feedback, and observe satisfaction trends over time.

## Main Objective

The main objective of this project is to provide a simple and interactive platform for understanding student opinions about campus services such as the Library, Cafeteria, Hostel, Sports Center, and WiFi.

It helps identify:

- Which facilities are performing well
- Which facilities need improvement
- How satisfaction differs by department
- How satisfaction changes by academic year
- General trends in student feedback

## Key Features

- Admin login page
- Protected dashboard access using browser `localStorage`
- Total response count
- Average satisfaction score
- Best performing facility
- Facility-wise satisfaction chart
- Facility response distribution chart
- Department-wise analysis
- Year-wise trend chart
- Time-based satisfaction trend chart
- Filters for facility, department, and year

## Technology Used

| Area | Technology |
| --- | --- |
| Frontend | HTML, CSS, JavaScript |
| Charts | Chart.js |
| Backend | Python, FastAPI |
| Data Handling | Pandas |
| Data Storage | CSV file |
| Server | Uvicorn |

## Project Modules

### Frontend

The frontend is stored in the `frontend/` folder.

- `login.html` provides the admin login screen.
- `index.html` provides the main analytics dashboard.

The dashboard fetches data from the backend API and uses JavaScript to calculate values for cards, filters, and charts.

### Backend

The backend is stored in the `backend/` folder.

- `app.py` contains the FastAPI application.
- It reads the CSV dataset using Pandas.
- It provides API endpoints for data, metrics, filtering, and login.

### Data

The data files are stored in the `data/` folder.

- `generate_data.py` creates sample student satisfaction records.
- `add_timestamp.py` adds timestamp values to the dataset.
- `student_satisfaction.csv` is the main dataset used by the backend.

### Analysis

The `notebooks/eda.py` file performs basic exploratory data analysis on the dataset, including missing values, unique values, average scores, and facility-wise response counts.

## Dataset Summary

The dataset contains student satisfaction responses with these columns:

| Column | Description |
| --- | --- |
| `student_id` | Unique ID for each response |
| `gender` | Student gender |
| `year` | Academic year |
| `department` | Student department |
| `facility` | Campus facility being reviewed |
| `satisfaction_score` | Rating from 1 to 5 |
| `timestamp` | Date and time of the response |

## API Summary

| Endpoint | Method | Description |
| --- | --- | --- |
| `/` | GET | Checks whether the backend is running |
| `/data` | GET | Returns all student satisfaction records |
| `/metrics` | GET | Returns total responses, average score, and best facility |
| `/filtered` | GET | Returns filtered records based on selected filters |
| `/login` | POST | Validates admin login credentials |

## Login Details

```text
Username: admin
Password: admin123
```

## How The Project Works

1. The dataset is generated using Python.
2. The CSV file stores all student satisfaction records.
3. FastAPI loads the CSV file using Pandas.
4. The frontend sends requests to the backend API.
5. The backend returns JSON data.
6. JavaScript processes the returned data.
7. Chart.js displays the insights visually on the dashboard.

## Learning Outcomes

This project demonstrates:

- Basic data generation using Python
- Data analysis using Pandas
- REST API development using FastAPI
- Frontend API integration using JavaScript
- Interactive chart creation using Chart.js
- Full-stack project organization
- Simple authentication flow
- Dashboard-based data visualization

## Current Limitations

- Login credentials are hardcoded.
- Data is stored in a CSV file instead of a database.
- Authentication is simple and not production-ready.
- The frontend uses a fixed backend URL.
- CSS and JavaScript are written inside HTML files.
- There is no automated test suite yet.

## Future Scope

- Add database support using MySQL, PostgreSQL, or SQLite.
- Add secure authentication with sessions or JWT.
- Add role-based access for admins and users.
- Add export options for reports.
- Deploy the backend and frontend online.
- Add predictive analytics or machine learning features.
- Improve frontend structure by separating HTML, CSS, and JavaScript.

## Conclusion

Campus Pulse Dashboard is a beginner-friendly but complete full-stack analytics project. It connects data processing, backend APIs, authentication, and frontend visualization into one working dashboard that can help campus administrators understand student satisfaction and make better decisions.

