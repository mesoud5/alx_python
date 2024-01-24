# IMPORTING MYSQLDB
import MySQLdb

host = "localhost"
user = "mesoud"
password = "aymen123"
database = "hbtn_0e_0_usa"

# Connect to MySQL server and specify the database
with MySQLdb.connect(
    host=host,
    user=user,
    passwd=password,
    db=database,
) as connection:
    cursor = connection.cursor()

    # Create the database if it doesn't exist
    new_database = "CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa"
    cursor.execute(new_database)
    connection.commit()
    use = "USE hbtn_0e_0_usa"
    cursor.execute(use)
    connection.commit()
    new_table = """CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
    );"""
    cursor.execute(new_table)
    connection.commit()
    insert = "INSERT INTO states (name) VALUES (%s), (%s)"
    values = ("California", "Arizona")
    cursor.execute(insert, values)
    connection.commit()

    # Select all states and display the results
    all_state = "SELECT id, name FROM states ORDER BY states.id"
    cursor.execute(all_state)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()  
    connection.close()


