# IMPORTING MYSQLDB
import MySQLdb

host = "localhost"
user = "mesoud"
password = "aymen123"
database = "hbtn_0e_0_usa"

# Connect to MySQL server and specify the database
connection = MySQLdb.connect(
    host=host,
    user=user,
    passwd=password,
    db=database,
)
cursor = connection.cursor()

   
use = "USE hbtn_0e_0_usa"
cursor.execute(use)
connection.commit()
# Execute the DELETE statement with a WHERE clause
delete_query = "DELETE FROM states WHERE id IN (%s, %s)"
condition_value = (3, 4)
cursor.execute(delete_query, condition_value)

# Commit the changes
connection.commit()
# Select all states and display the results
all_state = "SELECT id, name FROM states ORDER BY states.id"
cursor.execute(all_state)
states = cursor.fetchall()

for state in states:
        print(state)

cursor.close()  
connection.close()


