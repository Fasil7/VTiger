import sys
import subprocess

if len(sys.argv) != 3 or sys.argv[1] != "--restore":
    print("Usage: python restore.py --restore YYYY-MM-DD")
    sys.exit(1)

# Specify the date to restore
date_to_restore = sys.argv[2]
s3_backup_path = f"s3://fasilbucket/backups/{date_to_restore}-backup.tar.gz"
local_restore_path = f"/home/ubuntu/restorebackup{date_to_restore}-backup.tar.gz"

# Download the backup from S3
subprocess.run(["aws", "s3", "cp", s3_backup_path, local_restore_path])

# Extract the backup
subprocess.run(["tar", "-xzvf", local_restore_path, "-C", "/home/ubuntu/restorebackup"])

print(f"Restoration completed for {date_to_restore}. Data is in /home/ubuntu/restorebackup")


