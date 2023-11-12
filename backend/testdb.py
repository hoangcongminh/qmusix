import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect(
    "/home/namtran/projects/qmusix/backend/src/app.db"
)  # Replace 'your_database.db' with your database file path

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a query to retrieve the list of tables in the database
cursor.execute("SELECT * from user ")

# Fetch all the table names as a list
table_names = cursor.fetchall()

# Display the list of tables
for table_name in table_names:
    print(table_name)  # Access the first element in each tuple

# Close the cursor and the database connection
cursor.close()
conn.close()
