import csv
import pymysql
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection settings
hostname = "localhost"
username = "root"
password = "fasil1090405@"
dbname = "fasil"

# Create a database connection
conn = pymysql.connect(host=hostname, user=username, password=password, database=dbname)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Function to search for records
def search_records(key):
    try:
        # SQL query to search for records based on the key
        sql = "SELECT * FROM user_data WHERE firstname LIKE %s OR lastname LIKE %s OR email LIKE %s OR email2 LIKE %s OR profession LIKE %s"
        cursor.execute(sql, (f"%{key}%", f"%{key}%", f"%{key}%", f"%{key}%", f"%{key}%"))

        # Fetch and print the matching records
        results = cursor.fetchall()
        for row in results:
            print("ID:", row[0])
            print("First Name:", row[1])
            print("Last Name:", row[2])
            print("Email:", row[3])
            print("Email 2:", row[4])
            print("Profession:", row[5])
            print("-" * 20)

        logging.info("Search completed successfully!")

    except Exception as e:
        logging.error("Error:", e)

# Parse command line arguments
parser = argparse.ArgumentParser(description="Contact Management System")
parser.add_argument("--search", help="Search for records based on a key")
args = parser.parse_args()

if args.search:
    search_records(args.search)
else:
    logging.error("Invalid command. Please use '--search <key>' to search for records.")

# Close the cursor and the connection
cursor.close()
conn.close()
