import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''
             Create table Students (
                 S_id INT AUTO_INCREATMENT PRIMERY KEY,
                 S_name VARCHAR (40) NOT NULL,
                 S_add  VARCHAR (50) NOT NULL,
                 S_email VARCHAR (30) NOT NULL,
                 S_course VARCHAR (30) NOT NULL,
                 S_age INT NOT NULL   
             );
             
    ''')
conn.close()

