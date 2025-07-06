from mysql_connection import connect

def fetch_employees():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == "__main__":
    fetch_employees()
