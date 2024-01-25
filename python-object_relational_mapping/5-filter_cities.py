# IMPORTING MYSQLDB
import MySQLdb
import sys

username, password, database, states_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

connection = MySQLdb.connect(
    host="localhost",
    user=username,
    passwd=password,
    db=database,
)

cursor = connection.cursor()
cursor.execute("USE hbtn_0e_4_usa")
cities_in_state = "SELECT name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
cursor.execute(cities_in_state)
states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
connection.close()