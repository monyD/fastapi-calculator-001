docker build -t fastapi-calculator .
docker run -p 8000:8000 fastapi-calculator

# 🚀 FastAPI Calculator API (Dockerized)

A simple yet powerful calculator API built using FastAPI and fully containerized with Docker.

---

## 🧠 Project Overview

This project demonstrates a backend service built with FastAPI and deployed using Docker. It supports basic arithmetic operations and is designed as a beginner-friendly DevOps project.

---

## ⚙️ Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- Docker

---

## 📂 Project Structure
fastapi-calculator/
│── app/
│ └── main.py
│── Dockerfile
│── .gitignore
│── README.md


---

## 🚀 Run Locally (Without Docker)

```bash
pip install fastapi uvicorn
uvicorn app.main:app --reload

docker image build
docker build -t fastapi-calculator .

run container
docker run -p 8000:8000 fastapi-calculator

📌 API Endpoints
Operation	Endpoint
Add	/add?a=10&b=5
Subtract	/subtract?a=10&b=5
Multiply	/multiply?a=10&b=5
Divide	/divide?a=10&b=5


ERROR: 
!!!!!
{"error": "Cannot divide by zero"}


🎯 Learning Outcomes
Built REST API using FastAPI
Containerized application using Docker
Managed version control with Git
Published project on GitHub
🚀 Future Improvements
Add frontend UI
Add authentication
Store calculation history (database)
Deploy to AWS

👨‍💻 Author

Mony Dheeraj

