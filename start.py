import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

with open('start.sql','r') as f:
	sql = f.read()

for query in sql.split('-- ###'):
	c.execute(query)

conn.commit()
c.close()
conn.close()
