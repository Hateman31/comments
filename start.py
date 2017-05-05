import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

with open('start.sql','w') as f:
	sql = f.read()

print(sql[:100])	
c.execute(sql)

conn.commit()
c.close()
conn.close()
