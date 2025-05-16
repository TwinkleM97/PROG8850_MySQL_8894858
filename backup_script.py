# This script connects to the MySQL database and generates a timestamped backup 
# using mysqldump. It automates the backup process and creates a uniquely named .sql file each time it runs.

import os
import time
import subprocess

# Configurations
user = "root"
password = "Secret5555"
host = "127.0.0.1"
db_name = "prog8850_db"

# Generating a unique backup filename with timestamp
timestamp = time.strftime('%Y%m%d_%H%M%S')
backup_file = f"{db_name}_backup_{timestamp}.sql"

# Backup command using mysqldump
command = f"mysqldump -u {user} -p{password} -h {host} {db_name} > {backup_file}"

try:
    subprocess.run(command, shell=True, check=True)
    print(f" Backup successful: {backup_file}")
except subprocess.CalledProcessError as e:
    print(f" Backup failed: {e}")