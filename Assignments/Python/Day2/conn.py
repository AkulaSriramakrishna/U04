import sqlite3

conn = sqlite3.connect('sharktank.db')
conn.execute('''insert into emp values (1,'Rahul')''')
conn.commit()
print('Table created successfully')
conn.close()