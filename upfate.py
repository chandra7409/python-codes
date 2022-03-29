import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute( '''update student  set st_name='ramni' where set st_id=1''')
conn.commit()
conn.close()