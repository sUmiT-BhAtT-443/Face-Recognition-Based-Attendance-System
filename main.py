# Step 1: Create the employee table (if not already created)
from create_table import create_table
create_table()

# Step 2: Insert an employee (manual entry)
from insert_data import insert_employee

name = input("Enter employee name:")
address = input("Enter employee address: ")
insert_employee(name, address)

# Step 3: Fetch all employees (verify insert)
from fetch_all_data import fetch_employees
print("\nAll employees in database:")
fetch_employees()

# Step 4: Run face detection
import face_detect  # face_detect.py runs directly
from create_table import create_table
create_table()

