from tkinter import*
from PIL import Image,ImageTk
from course import CourseClass
from student import StudentClass
from result import resultClass
from ViewResult import report
import sqlite3 as sq
def create_db():
    con = sq.connect(database="rms.db")
    cur = con.cursor()
    #Table Creation for Course Page
    cur.execute("Create table if not exists course(cid INTEGER primary key AutoIncrement,name text,duration text, charges text,description text)")
    con.commit()

    #Table Creation for Student Page
    cur.execute("CREATE TABLE IF NOT EXISTS student(gr_no text PRIMARY KEY ,name text,email text, gender text,dob text,contact text,admission text,course text,year  text,roll text,address text)")
    con.commit()

    #Table Creation for Result Page
    cur.execute("Create table if not exists result(rid INTEGER primary key AutoIncrement,roll text,name text, course text,marks_obtain text,full_marks text,percentage text)")
    con.commit()

    #Table Creation for Sign_Up Page
    cur.execute("Create table if not exists AllUsers(eid INTEGER primary key AutoIncrement,f_name text,l_namen text, contact text, email text, question text, answer text, password text,u_name text)")
    con.commit()


    con.close()
    
create_db()

class RMS :
    def __init__(self,root):
        self.root = root
        self.root.title("Student DBMS")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        title=Label(self.root,text="Student Database Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

        M_Frame=LabelFrame(self.root,text="Menu:",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0002FF",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0002FF",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0002FF",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Student Results",font=("goudy old style",15,"bold"),bg="#0002FF",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0002FF",fg="white",cursor="hand2").place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0002FF",fg="white",cursor="hand2").place(x=1120,y=5,width=200,height=40)
        
        footer=Label(self.root,text="RGIT : Student Database Management System\n  Contact us for anyTechnical Issue:98xxxxxxxxx",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM ,fill=X)

        self.bg_img=Image.open("images/bg.jpg")
        self.bg_img=self.bg_img.resize((563,375),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_img=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#1E90FF",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)
        self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#1E90FF",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)
        self.lbl_result=Label(self.root,text="Total Results\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#1E90FF",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=report(self.new_win)
    

if __name__ ==  "__main__":
    root=Tk()
    obj = RMS(root)
    root.mainloop()

