#!/bin/bash

# Set your GitHub repository URL and AWS S3 bucket name
GITHUB_REPO_URL="https://github.com/Fasil7/Capstone.git"
S3_BUCKET="fasilbucket"
BACKUP_FOLDER="/home/ubuntu/gitbackup"
DATE=$(date '+%Y-%m-%d')

# Function to perform the backup
perform_backup() {
    # Clone or pull the GitHub repository
    if [ ! -d "$BACKUP_FOLDER" ]; then
        git clone $GITHUB_REPO_URL $BACKUP_FOLDER
    else
        cd $BACKUP_FOLDER
        git pull
    fi

    # Create a backup archive
    tar -czvf "$BACKUP_FOLDER/$DATE-backup.tar.gz" $BACKUP_FOLDER

    # Upload the backup to AWS S3
    aws s3 cp "$BACKUP_FOLDER/$DATE-backup.tar.gz" "s3://$S3_BUCKET/backups/$DATE-backup.tar.gz"
    
    # Clean up old backups if needed
    # Implement logic to keep the last 7 days' backups and delete older ones
}

# Perform a full backup on Sundays, incremental backups on other days
if [ $(date '+%A') == "Sunday" ]; then
    perform_backup
else
    # Check if a full backup exists for today (Sunday) and perform an incremental backup
    if [ ! -f "$BACKUP_FOLDER/$DATE-backup.tar.gz" ]; then
        perform_backup
    fi
fi


