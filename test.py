import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

query = '''
select * from cities
'''

for x in c.execute(query):
	print(x)

conn.commit()
c.close()
conn.close()
