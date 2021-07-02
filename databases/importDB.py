"""
Simple sqlite actions in python3 with sqlite

@Author Alvis Grigaļūns <alvisgrigaluns@gmail.com>
"""

import sqlite3

# connects with sqlite database
conn = sqlite3.connect("chinook.db")

# create table in sqlite
cursor = conn.cursor()
cursor.execute("CREATE TABLE synths (name TEXT, series TEXT, product_number INTEGER)")

# insert values in synths table
cursor.execute("INSERT INTO gear VALUES ('Elektron', 'rytm', 186750)")
cursor.execute("INSERT INTO gear VALUES ('Korg', 'volca', 210034)")
cursor.execute("INSERT INTO gear VALUES ('Erica synths', 'picosystem', 133900)")

# output all rows from synths table
rows = cursor.execute("SELECT name, series, product_number FROM synths").fetchall()

print(rows)

# output only names from synths table
"""
target_synths_name = "Elektron"
rows = cursor.execute(
    "SELECT name, series, product_number FROM synths WHERE name = ?",
    (target_synths_name,),
).fetchall()

print(rows)
"""

# modifying data in table
"""
new_product_number = 2
new_synths_name = "Novation"
cursor.execute(
    "UPDATE synths SET product_number = ? WHERE name = ?",
    (new_product_number, new_synths_name)
)
"""
