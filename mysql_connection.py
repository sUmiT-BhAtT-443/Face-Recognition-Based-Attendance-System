import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",           #MySQL user
        password="sumit@123",   # sql password
        database="face_db"     # database_name
    )
    return conn
