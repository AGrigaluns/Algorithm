"""
    @Author Alvis Grigaļūns <alvisgrigaluns@gmail.com>

    This file contains migration from Sqlite to MySQL
"""

import mysql.connector as mysql
from mysql.connector import Error
import sqlite3

# check if there was no error during connection
try:
    shopDB = mysql.connect(
        host="localhost",
        user="root",
        database="musicshop",
        passwd="**********"
    )
    if shopDB.is_connected():
        db_Info = shopDB.get_server_info()
        print("Connected to MySQL Server", db_Info)

except Error as e:
    print("Error while connecting to MySQL", e)

conn = sqlite3.connect("chinook.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_db WHERE type='table'")
result = cursor.fetchall()
cursor.execute("SET FOREIGN_KEY_CHECKS=0")




