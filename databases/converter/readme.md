Run this to convert your file:
sqlite3 chinook.db .dump | python3 converter.py > output.sql