import sqlite3
conn = sqlite3.connect('factbook.db')

c = conn.cursor()
newdata = c.execute('SELECT * FROM facts ORDER BY population LIMIT 10;').fetchall()

print(newdata)
