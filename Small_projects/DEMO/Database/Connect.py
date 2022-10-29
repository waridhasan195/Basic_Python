

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mySqlpass123",
    database = "testdb"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE testdb")


# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)


# # mycursor.execute("CREATE TABLE students (name VARCHAR(255), Age INTEGER(10))")
# mycursor.execute("SHOW TABLES")

# for tb in mycursor:
#     print(tb)


sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
students = [("Rachel", 22),
            ("Liton", 29),
            ("Tamim", 31),
            ("Riad", 30),
            ("Mushfiq", 31),
            ("Shakib", 35),
            ("Mustafiz", 19)]
mycursor.executemany(sqlFormula, students)
mydb.commit()
