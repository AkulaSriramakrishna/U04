import sqlite3

conn = sqlite3.connect('sharktank.db')
conn.execute('''insert into test values (2,'Rahul')''')
conn.commit()
print('Table created successfully')
conn.close()