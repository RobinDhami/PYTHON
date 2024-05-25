import mysql.connector

# Connect to the MySQL server
db = mysql.connector.connect(
    host="localhost",
    port=3300,
    user="root",
    passwd="root",
    database="customer"
)

cursor = db.cursor()

# Define the CREATE TABLE query
create_table_query = """
CREATE TABLE IF NOT EXISTS customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
)
"""

# Execute the CREATE TABLE query
cursor.execute(create_table_query)

name= input("Enter your name: ")
email = input("Enter your name: ")

insert_customer =""" INSERT INTO  customer(name,email) value (%s,%s)
"""

cursor.execute(insert_customer,((name,email)))

# Commit changes
db.commit()

# Execute a SELECT query to fetch data from the "customer" table
select_query = "SELECT * FROM customer"
cursor.execute(select_query)

result = cursor.fetchall()
# Print the column names
print("ID\tName\tEmail")
print("-" * 30)

# Print the data
for row in result:
    print(f"{row[0]}\t{row[1]}\t{row[2]}")
# Close cursor and connection
cursor.close()
db.close()

print("Table created successfully.")
