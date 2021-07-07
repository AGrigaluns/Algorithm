import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    database="musicshop",
    passwd="**********"
)

print(db)


