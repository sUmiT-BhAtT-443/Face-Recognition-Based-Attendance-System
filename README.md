# 👨‍💻 Face Recognition-Based Attendance System

This project automates employee attendance using face recognition.
It captures the face using **OpenCV**, stores data into **MySQL**, and marks them as **Present**.

## 🔧 Technologies Used
- Python
- OpenCV
- MySQL

## 🚀 How It Works
1. System asks for employee name and address
2. Face is detected in live webcam using Haar Cascades
3. The employee is marked as "Present" and added to the database

## 📸 Output Screenshot

### ➤ Face Detection
![Face Detection]![camera_detection](https://github.com/user-attachments/assets/3f606530-9381-46f3-b1b1-070de35927ed)


### ➤ Terminal Output
![Terminal Output]![terminal_output](https://github.com/user-attachments/assets/396c6333-ab2b-4962-b228-19b2b407ee7a)


## 📂 Files in this Repo
- `main.py` – Main file to run full system
- `face_detect.py` – Face detection and DB insert
- `mysql_connection.py` – DB connection
- `insert_data.py` – Insert employee data
- `create_table.py` – Create employee table
- `fetch_all_data.py` – Fetch all records

---

## 📌 Note
Make sure MySQL server is running and OpenCV is installed before running the project.

