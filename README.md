# Interview_Question_Generator
Interview Question Generator built using Python, Streamlit, and SQL Server. Features question practice, mock interviews, progress tracking, and performance analytics for technical interview preparation.

# 🎯 Interview Question Generator

## Overview

Interview Question Generator is a web-based application designed to help students and job seekers prepare for technical interviews. The platform provides categorized interview questions, mock interview sessions, progress tracking, and performance analytics.

The project is built using **Python**, **Streamlit**, and **SQL Server**.

---

## Features

### 📚 Question Generation

* Filter questions by Technology
* Filter questions by Topic
* Filter questions by Difficulty
* View detailed answers
* Mark questions as attempted

### 🎤 Mock Interview

* Random interview question generation
* Interactive interview simulation
* Progress tracking during interviews
* Multiple interview rounds

### 📊 Analytics Dashboard

* Total questions available
* Attempted questions count
* Pending questions count
* Completion percentage
* Technology-wise attempt analysis
* Most practiced technology

### 🗄 Database Integration

* SQL Server database
* Stores interview questions
* Tracks user attempts
* Maintains performance records

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* Microsoft SQL Server

### Libraries

* Pandas
* PyODBC
* Streamlit

---

## Database Schema

### Questions Table

| Column      | Description                |
| ----------- | -------------------------- |
| Question_ID | Unique question identifier |
| Technology  | Technology category        |
| Topic       | Topic category             |
| Difficulty  | Easy / Medium / Hard       |
| Question    | Interview question         |
| Answer      | Expected answer            |

### Attempts Table

| Column       | Description               |
| ------------ | ------------------------- |
| Attempt_ID   | Unique attempt identifier |
| User_ID      | User identifier           |
| Question_ID  | Attempted question        |
| Status       | Attempt status            |
| Attempt_Date | Date and time of attempt  |

---

## Project Structure

```text
Interview_Question_Generator/
│
├── streamlit_app.py
├── db.py
├── import_questions.py
├── questions.csv
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Interview_Question_Generator
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Database

Create the required SQL Server database and tables.

### Questions Table

```sql
CREATE TABLE Questions
(
    Question_ID INT IDENTITY(1,1) PRIMARY KEY,
    Technology VARCHAR(100),
    Topic VARCHAR(100),
    Difficulty VARCHAR(50),
    Question TEXT,
    Answer TEXT
);
```

### Attempts Table

```sql
CREATE TABLE Attempts
(
    Attempt_ID INT IDENTITY(1,1) PRIMARY KEY,
    User_ID INT NOT NULL,
    Question_ID INT NOT NULL,
    Status VARCHAR(20),
    Attempt_Date DATETIME DEFAULT GETDATE(),

    FOREIGN KEY (Question_ID)
    REFERENCES Questions(Question_ID)
);
```

---

## Run Application

```bash
streamlit run streamlit_app.py
```

---

## Future Enhancements

* User Authentication
* AI-generated Interview Questions
* Interview Scoring System
* Personalized Recommendations
* Cloud Deployment
* Resume-based Question Generation

---

## Learning Outcomes

Through this project, the following concepts were implemented:

* Python Programming
* Streamlit Development
* SQL Server Integration
* CRUD Operations
* Database Design
* Data Analytics
* User Interface Development

---

## Author

Tanvi Mathur

Engineering Student Project

