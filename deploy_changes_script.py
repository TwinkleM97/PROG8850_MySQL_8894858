# This script connects to the MySQL database and deploys schema changes.
# It creates the Employee table if it does not exist and adds the 'email' column only if it is not already present.

import mysql.connector

config = {
    'user': 'root',
    'password': 'Secret5555',
    'host': '127.0.0.1',
    'database': 'prog8850_db'
}

# SQL 1: Creating table if it doesn't exist
create_table_sql = """
CREATE TABLE IF NOT EXISTS Employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    department VARCHAR(255),
    hire_date DATE
);
"""

# SQL 2: Adding column if not exists
add_column_sql = """
ALTER TABLE Employee ADD COLUMN email VARCHAR(255);
"""

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute(create_table_sql)
    print("Table 'Employee' has been created if it did not already exist.")

    # Checking if the 'email' column already exists
    cursor.execute("""
        SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS
        WHERE table_name = 'Employee' AND column_name = 'email';
    """)
    if cursor.fetchone()[0] == 0:
        cursor.execute(add_column_sql)
        print("Column 'email' has been added to the Employee table.")
    else:
        print("Column 'email' already exists in the Employee table. No changes were made.")

    conn.commit()

except mysql.connector.Error as err:
    print("An error occurred while deploying the changes:", err)

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
