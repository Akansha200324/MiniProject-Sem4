from tkinter import*
from PIL import Image , ImageTk
from tkinter import ttk,messagebox
import sqlite3 as sq
class StudentClass :
    def __init__(self,root):
        self.root = root
        self.root.title("Student DBMS")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="pink")
        self.root.focus_force()

        title=Label(self.root,text="RGIT : Manage Student Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)

        #============================ Variables ===========================================================================

        self.var_gr_no=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()

        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()

        self.var_year=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()

        #====================================== Widgets =======================================================================

        lbl_gr_no=Label(self.root,text="GR no.",font=("goudy old style",15,"bold"),bg="#E6E6FA").place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="#E6E6FA").place(x=10,y=100)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="#E6E6FA").place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="#E6E6FA").place(x=10,y=180)
        lbl_year=Label(self.root,text="Year",font=("goudy old style",15,"bold"),bg="#E6E6FA").place(x=10,y=220)
        
        #lbl_div=Label(self.root,text="Div",font=("goudy old style",15,"bold"),bg="#E6E6FA").place(x=310,y=220)
        #txt_div=Entry(self.root,textvariable= self.var_div,font=("goudy old style",15,"bold"),bg="#E0FFFF").place(x=380,y=60,width=50)

        lbl_roll=Label(self.root,text="Roll no.",font=("goudy old style",15,"bold"),bg="#E6E6FA").place(x=360,y=220)
        txt_roll=Entry(self.root,textvariable= self.var_roll,font=("goudy old style",15,"bold"),bg="#E0FFFF").place(x=480,y=220,width=200)

        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="#E6E6FA").place(x=10,y=260)

        #--------------------------------------------------------------------------------------------------------------------------

        lbl_dob=Label(self.root,text="DoB",font=("goudy old style",15,"bold"),bg="#E6E6FA").place(x=360,y=60)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="#E6E6FA").place(x=360,y=100)
        lbl_admission=Label(self.root,text="Admission",font=("goudy old style",15,"bold"),bg="#E6E6FA").place(x=360,y=140)
        lbl_course=Label(self.root,text="Department",font=("goudy old style",15,"bold"),bg="#E6E6FA").place(x=360,y=180)
        
    
        #======================================== Entey Fields ===================================================================

        self.txt_gr_no=Entry(self.root,textvariable= self.var_gr_no,font=("goudy old style",15,"bold"),bg="#E0FFFF")
        self.txt_gr_no.place(x=150,y=60,width=200)

        txt_name=Entry(self.root,textvariable= self.var_name,font=("goudy old style",15,"bold"),bg="#E0FFFF").place(x=150,y=100,width=200)
        txt_email=Entry(self.root,textvariable= self.var_email,font=("goudy old style",15,"bold"),bg="#E0FFFF").place(x=150,y=140,width=200)

        self.txt_gender=ttk.Combobox(self.root,textvariable= self.var_gender,values=("Select","Male","Female","Others"),font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150,y=180,width=200)
        self.txt_gender.current(0)

        #------------------------------------------------------------------------------------------------------------------------

        self.txt_dob=Entry(self.root,textvariable= self.var_dob,font=("goudy old style",15,"bold"),bg="#E0FFFF").place(x=480,y=60,width=200)
        txt_contact=Entry(self.root,textvariable= self.var_contact,font=("goudy old style",15,"bold"),bg="#E0FFFF").place(x=480,y=100,width=200)
        txt_admission=Entry(self.root,textvariable= self.var_a_date,font=("goudy old style",15,"bold"),bg="#E0FFFF").place(x=480,y=140,width=200)

        self.txt_year=ttk.Combobox(self.root,textvariable= self.var_year,values=("Select","1st Year","2nd Year","3rd Year","4th Year"),font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_year.place(x=150,y=220,width=150)
        self.txt_year.current(0)

        #------------------------------------------Fetch course-------------------------------------------------------------------
        self.course_list= []
        self.fetch_course() #fetch_course

        self.txt_course=ttk.Combobox(self.root,textvariable= self.var_course,values=(self.course_list),font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_course.place(x=480,y=180,width=200)
        self.txt_course.set("Select")

        #------------------------------------------------------------------------------------------------------------------------

        

        #======================================= Text address ============================================================

        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="#E0FFFF")
        self.txt_address.place(x=150,y=260,width=500,height=100)

        #======================================== Buttons ===============================================================================================================
        
        self.btn_add=Button(self.root,text='Save',font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        #================= Search panel ===================================

        self.var_search=StringVar()
        lbl_search_gr_no=Label(self.root,text="GR Number",font=("goudy old style",15,"bold"),bg="#E6E6FA").place(x=720,y=60)
        txt_search_gr_no=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="#E0FFFF").place(x=870,y=60,width=180)
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)  
           
        #================= content ========================================

        self.C_Frame = Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)  

        scrolly=Scrollbar(self.C_Frame , orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame , orient=HORIZONTAL)


        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("gr_no","name","email","gender","dob","contact","admission","course","year","roll","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM , fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("gr_no",text="GR no.")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="DoB")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("admission",text="Admission")
        self.CourseTable.heading("course",text="Department")
        self.CourseTable.heading("year",text="Year")
        self.CourseTable.heading("roll",text="Roll no.")
        self.CourseTable.heading("address",text="Address")

        self.CourseTable["show"]='headings'

        self.CourseTable.column("gr_no",width=80)
        self.CourseTable.column("name",width=150)
        self.CourseTable.column("email",width=150)
        self.CourseTable.column("gender",width=50)
        self.CourseTable.column("dob",width=100)
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("admission",width=100)
        self.CourseTable.column("course",width=100)
        self.CourseTable.column("year",width=60)
        self.CourseTable.column("roll",width=50)
        self.CourseTable.column("address",width=200)
        
        self.CourseTable.pack(fill=BOTH,expand=1)


        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        

#=============================================================================================================================================================



    def clear(self):
        self.show()
        self.var_gr_no.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("Select")
        self.var_year.set("")
        self.var_roll.set("")
        self.txt_address.delete("1.0",END) 
        self.txt_gr_no.config(state=NORMAL)
        self.var_search.set("") 
        
    def delete(self):
        con = sq.connect(database="ResultManagementSystem.db")
        cur = con.cursor()
        try:
            if self.var_gr_no.get()=="":
                messagebox.showerror("Error","GRno. is required",parent=self.root)
            else:
                cur.execute("select * from course where gr_no=?",(self.var_gr_no.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select student from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student  where gr_no=?",(self.var_gr_no.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")

    def get_data(self,ev):
        self.txt_gr_no.config(state='readonly')
        r  =  self.CourseTable.focus()
        content= self.CourseTable.item(r)
        row=content["values"]
        self.var_gr_no.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])
        self.var_year.set(row[8])
        self.var_roll.set(row[9])
        self.txt_address.delete("1.0",END) 
        self.txt_address.insert(END,row[10])


    def add(self):
        con = sq.connect(database="ResultManagementSystem.db")
        cur = con.cursor()
        try:
            if self.var_gr_no.get()=="":
                messagebox.showerror("Error","GR no. is to be required",parent=self.root)
            else:
                cur.execute("select * from student where gr_no=?",(self.var_gr_no.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","GR no. already present",parent=self.root)
                else:
                    cur.execute("insert into student( gr_no , name , email , gender , dob , contact , admission , course , year , roll , address ) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_gr_no.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_roll.get(),
                        self.txt_address.get("1.0",END) ))
                    con.commit()
                    messagebox.showinfo("Success","Student added successfully",parent=self.root)
                    self.show()
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")


    def update(self):
        con = sq.connect(database="ResultManagementSystem.db")
        cur = con.cursor()
        try:
            if self.var_gr_no.get()=="":
                messagebox.showerror("Error","GR no. is to be required",parent=self.root)
            else:
                cur.execute("select * from student where gr_no=?",(self.var_gr_no.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("update student set name=? , email=? , gender=? , dob=? , contact=? , admission=? , course=? , year=? , roll=? , address=? where gr_no=? ",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_roll.get(),
                        self.txt_address.get("1.0",END),
                        self.var_gr_no.get() ))
                    con.commit()
                    messagebox.showinfo("Success","Student update successfully",parent=self.root)
                    self.show()

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")


    def show(self):
        con = sq.connect(database="ResultManagementSystem.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
               
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")

    def fetch_course(self):
        con = sq.connect(database="ResultManagementSystem.db")
        cur = con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
               
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")


    def search(self):
        con = sq.connect(database="ResultManagementSystem.db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from student where gr_no=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None :
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
               
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")


if __name__ ==  "__main__":
    root=Tk()
    obj = StudentClass(root)
    root.mainloop()
