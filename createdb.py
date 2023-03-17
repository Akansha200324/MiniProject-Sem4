import sqlite3 as sq
def create_db():
    con = sq.connect(database="ResultManagementSystem.db")
    cur = con.cursor()
    #Table Creation for Course Page
    cur.execute("Create table if not exists course(cid INTEGER primary key AutoIncrement,name text,duration text, charges text,description text)")
    cur.execute("SELECT * FROM course")
    print(cur.fetchall())

    #Table Creation for Student Page
    cur.execute("CREATE TABLE IF NOT EXISTS student(gr_no text PRIMARY KEY ,name text,email text, gender text,dob text,contact text,admission text,course text,year  text,roll text,address text)")
    con.commit()

    #Table Creation for Result Page
    cur.execute("Create table if not exists result(rid INTEGER primary key AutoIncrement,gr_no text,name text, course text,marks_obtain text,full_marks text,percentage text)")
    con.commit()

    
    #Table Creation for Sign_Up Page
    cur.execute("Create table if not exists AllUsers(eid INTEGER primary key AutoIncrement,f_name text,l_namen text, contact text, email text, question text, answer text, password text,u_name text)")
    con.commit()


    con.close()
    
create_db()