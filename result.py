from tkinter import*
from PIL import Image , ImageTk
from tkinter import ttk,messagebox
import sqlite3
class resultClass :
    def __init__(self,root):
        self.root = root
        self.root.title("Student DBMS")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="pink")
        self.root.focus_force()

        title=Label(self.root,text="RGIT : Add Student Result Details",font=("goudy old style",20,"bold"),bg="yellow",fg="black").place(x=10,y=15,width=1180,height=35)

    #========================= Labels ====================================================

    #Variables
        self.var_gr_no=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.gr_no_list=[]
    # Function calling from fetch
        self.fetch_gr_no()

    #Sections
        lbl_select = Label(self.root,text="Select Student",font=("times new roman",20,"bold"),bg="white").place(x=50,y=100)
        lbl_name = Label(self.root,text="Name",font=("times new roman",20,"bold"),bg="white").place(x=50,y=160)
        lbl_course = Label(self.root,text="Department",font=("times new roman",20,"bold"),bg="white").place(x=50,y=220)
        lbl_marks = Label(self.root,text="Marks Obtained",font=("times new roman",20,"bold"),bg="white").place(x=50,y=280)
        lbl_full_marks = Label(self.root,text="Full Marks",font=("times new roman",20,"bold"),bg="white").place(x=50,y=340)

        self.student1 = ttk.Combobox(self.root,textvariable=self.var_gr_no,values=self.gr_no_list,font=("times new roman",15,"bold"),state="readonly",justify=CENTER)
        self.student1.place(x=280,y=100,width=200)
        self.student1.set("Select")
        
        btn_search=Button(self.root,text="Search",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.search).place(x=500,y=100,width=100,height=28)

        txt_name = Entry(self.root,textvariable=self.var_name,font=("times new roman",20,"bold"),bg="lightyellow",state="readonly").place(x=280,y=160,width=320,height=30)
        txt_course = Entry(self.root,textvariable=self.var_course,font=("times new roman",20,"bold"),bg="lightyellow",state="readonly").place(x=280,y=220,width=320,height=30)
        txt_marks = Entry(self.root,textvariable=self.var_marks,font=("times new roman",20,"bold"),bg="lightyellow").place(x=280,y=280,width=320,height=30)
        txt_full_marks = Entry(self.root,textvariable=self.var_full_marks,font=("times new roman",20,"bold"),bg="lightyellow").place(x=280,y=340,width=320,height=30)

    #Buttons
        self.add=Button(self.root,text="Submit",font=("times new roman",15,"bold"),bg="lightblue",activebackground="lightblue",cursor="hand2",command=self.add)
        self.add.place(x=300,y=420,width=120,height=35)
        self.clear=Button(self.root,text="Clear",font=("times new roman",15,"bold"),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)

    #Image
        self.bgImage=Image.open("images/result.png")
        self.bgImage=self.bgImage.resize((530,300),Image.ANTIALIAS)
        self.bgImage=ImageTk.PhotoImage(self.bgImage)

        self.lbl_bg=Label(self.root,image=self.bgImage).place(x=640,y=100)

# Fetch to show gr_no no. in select student tab
    def fetch_gr_no(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            cur.execute("Select gr_no from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.gr_no_list.append(row[0])
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#For Search tab functioning
    def search(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            cur.execute("Select name,course from student where gr_no=?",(self.var_gr_no.get(),))
            row=cur.fetchone()
            if row !=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record Found",parent=self.root)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def add(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please First Search Student Record",parent=self.root)
            else:
                cur.execute("Select * from result where gr_no=? and course=?",(self.var_gr_no.get(),self.var_course.get())) #Due to tupple we added , at last
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error, Result already Present",parent=self.root)
                else:
                    percentage=(int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                    cur.execute("Insert into result(gr_no,name,course,marks_obtain,full_marks,percentage) values(?,?,?,?,?,?)",(
                        self.var_gr_no.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(percentage)
                        
                    ) )
                    conn.commit()
                    messagebox.showinfo("Great","Result Added Successfully",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def clear(self):
        self.var_gr_no.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_full_marks.set("")


if __name__ ==  "__main__":
    root=Tk()
    obj = resultClass(root)
    root.mainloop()

