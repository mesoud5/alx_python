# IMPORTING MYSQLDB
import MySQLdb
import sys

# Extract MySQL credentials from command line arguments
if len(sys.argv) != 5:
    print("Usage: python script.py <username> <password> <database>")
    sys.exit(1)

username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

# Connect to MySQL server and specify the database
connection = MySQLdb.connect(
    host="localhost",
    user=username,
    passwd=password,
    db=database
)

cursor = connection.cursor()

# Select all states and display the results
all_state = "SELECT id, name FROM states WHERE name = %s COLLATE utf8mb4_bin ORDER BY states.id ASC"
cursor.execute(all_state, (state_name,))
states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
connection.close()
