from mysql_connection import connect

def insert_employee(name, address, status="Absent"):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO employees (name, address, status) VALUES (%s, %s, %s)", (name, address, status))
    conn.commit()
    conn.close()
    print("Employee added successfully.")

# Optional testing block
if __name__ == "__main__":
    name = input("Enter name: ")
    address = input("Enter address: ")
    insert_employee(name, address)
