from mysql_connection import connect

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            address VARCHAR(200),
            status VARCHAR(20) DEFAULT 'Absent'
        )
    """)

    conn.commit()
    conn.close()
    print("Employee table created successfully.")

if __name__ == "__main__":
    create_table()
 