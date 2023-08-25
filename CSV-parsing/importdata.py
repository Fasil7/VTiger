import csv
import pymysql
import logging

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

# Path to CSV file
csvFilePath = '/home/ubuntu/CSV/myFile0.csv'

try:
    # Open the CSV file
    with open(csvFilePath, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        batch_size = 100  # Number of rows to insert in one batch
        batch = []  # To accumulate rows for batch insertion

        for row in csvreader:
            id = row['id']
            first_name = row['firstname']
            last_name = row['lastname']
            email = row['email']
            email2 = row['email2']
            profession = row['profession']

            # Append data to the batch
            batch.append((id, first_name, last_name, email, email2, profession))

            if len(batch) >= batch_size:
                # SQL query to insert data into the database using parameterized query
                sql = "INSERT INTO user_data (Id, firstname, lastname, email, email2, profession) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.executemany(sql, batch)
                conn.commit()
                batch = []  # Clear the batch for the next set of rows

        # Insert any remaining rows in the batch
        if batch:
            sql = "INSERT INTO user_data (Id, firstname, lastname, email, email2, profession) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.executemany(sql, batch)
            conn.commit()

        logging.info("Data imported and saved to the database successfully!")

except Exception as e:
    conn.rollback()
    logging.error("Error:", e)

finally:
    # Close the cursor and the connection
    cursor.close()
    conn.close()
