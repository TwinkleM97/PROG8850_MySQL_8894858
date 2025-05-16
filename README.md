# PROG8850 – Assignment 1-Week 1: Database Automation and Scripting

### Name: Twinkle Akhilesh Mishra
### Student ID: 8894858 

## Requirements
Make sure the following are installed:
- MySQL Server (8.0+)
- Python 3.11+
- `mysql-connector-python` library

Install the Python MySQL connector if needed:
```bash
pip install mysql-connector-python
```

---

## Setup MySQL Server

If using Ansible:

Start the MySQL container:
```bash
ansible-playbook up.yml
```

To access MySQL:
```bash
mysql -u root -h 127.0.0.1 -p
```

To shut down the container:
```bash
ansible-playbook down.yml
```

---

## Scripts Included

### 1. `backup_script.py`

- Creates a timestamped `.sql` backup of the database.
- Uses `mysqldump` and stores the file in the current directory.

Edit these variables in the script if needed:
```python
user = "root"
password = "Secret5555"
db_name = "prog8850_db"
```

To run:
```bash
python backup_script.py
```

---

### 2. `deploy_changes_script.py`

- Connects to the MySQL database
- Creates the `Employee` table if it does not exist
- Adds a new `email` column if it's not already present

To run:
```bash
python deploy_changes_script.py
```

---

## To Verify

### View tables in MySQL:
```sql
USE prog8850_db;
SHOW TABLES;
DESCRIBE Employee;
```

### View backups:

After running `backup_script.py`, a file like this will appear:
```
prog8850_db_backup_YYYYMMDD_HHMMSS.sql
```

Open it in any text editor to confirm the `Employee` table and `email` column are included.

---

## Final Notes

These scripts are designed to automate routine database tasks:
- `backup_script.py` can be scheduled for daily backups.
- `deploy_changes_script.py` helps maintain schema changes programmatically.

This project demonstrates automation in database administration using Python.
