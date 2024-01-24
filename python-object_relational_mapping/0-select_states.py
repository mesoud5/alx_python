import MySQLdb
host = "localhost"
user = "root"
password = "aymen123"
connection = MySQLdb.connect(
    host=host,
    user=user,
    passwd=password
)
cursor = connection.cursor()
new_database = "CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa"
cursor.execute(new_database)
connection.commit()
all_state = "SELECT id, name FROM states ORDER BY states.id"
cursor.execute(all_state)
states = cursor.fetchall()
cursor.close()
connection.close()
