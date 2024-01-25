# IMPORTING MYSQLDB
import MySQLdb
import sys

# Extract MySQL credentials from command line arguments
if len(sys.argv) != 4:
    print("Usage: python script.py <username> <password> <database>")
    sys.exit(1)

username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

# Connect to MySQL server and specify the database
connection = MySQLdb.connect(
    host="localhost",
    user=username,
    passwd=password,
    db=database,
)

cursor = connection.cursor()

# Select all states and display the results
all_cities = "SELECT id, name, FROM cities ORDER BY cities.id ASC"
cursor.execute(all_cities)
cities = cursor.fetchall()

for city in cities:
    print(city)

cursor.close()
connection.close()
