import sqlite3
conn=sqlite3.connect("sqlite.db")
ins='''
insert into Students ( S_id,S_name,S_add,S_email, S_course,S_age) values 
( '283','Tilak','Gurugnawa',"tilakc3432@gmail.com",'btech',26)
    
'''
conn.execute(ins)
conn.commit()
conn.close()