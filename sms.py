from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox
import pymysql
from PIL.EpsImagePlugin import field

from login import usernameLabel


#functionality

def exit_student():
    answer = messagebox.askyesno('Confirm Exit', 'Do you really want to exit?')
    if answer:
        root.destroy()




def update_student():
    update_window = Toplevel()
    update_window.title('Update Student')
    update_window.grab_set()
    update_window.resizable(False, False)

    # Variables
    global original_id
    original_id = StringVar()

    # --- Labels and Entries ---
    idLabel = Label(update_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(update_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(update_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(update_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    dobLabel = Label(update_window, text='DOB', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=5, column=1, pady=15, padx=10)

    genderLabel = Label(update_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=6, column=1, pady=15, padx=10)

    # --- Function to update data ---
    def update_data():
        date = time.strftime('%d/%m/%Y')
        currenttime = time.strftime('%H:%M:%S')

        query = '''
            UPDATE student 
            SET id=%s, name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s 
            WHERE id=%s
        '''
        values = (
            idEntry.get(),
            nameEntry.get(),
            phoneEntry.get(),
            emailEntry.get(),
            addressEntry.get(),
            genderEntry.get(),
            dobEntry.get(),
            date,
            currenttime,
            original_id.get()  # Using the original ID here
        )

        mycursor.execute(query, values)
        con.commit()
        messagebox.showinfo('Success', f'Id {original_id.get()} updated successfully!')
        update_window.destroy()
        show_student()

    # --- Button to trigger update ---
    update_student_button = ttk.Button(update_window, text='UPDATE', command=update_data)
    update_student_button.grid(row=7, columnspan=2, pady=15)

    # --- Pre-fill data from selected row ---
    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    listdata = content['values']

    idEntry.insert(0, listdata[0])
    nameEntry.insert(0, listdata[1])
    phoneEntry.insert(0, listdata[2])
    emailEntry.insert(0, listdata[3])
    addressEntry.insert(0, listdata[4])
    genderEntry.insert(0, listdata[5])
    dobEntry.insert(0, listdata[6])





def show_student():
    query = 'SELECT * FROM student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def delete_student():
    indexing = studentTable.focus()
    if not indexing:
        messagebox.showerror('Error', 'Please select a student to delete')
        return
    content = studentTable.item(indexing)
    content_id = content['values'][0]
    query = 'DELETE FROM student WHERE id=%s'
    mycursor.execute(query, (content_id,))
    con.commit()
    messagebox.showinfo('Deleted', f'Id {content_id} is deleted successfully')
    # Refresh table
    query = 'SELECT * FROM student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)


def search_student():
    def search_data():
        query = 'SELECT * FROM student WHERE id=%s OR name=%s OR email=%s OR mobile=%s OR address=%s OR gender=%s OR dob=%s'
        mycursor.execute(query, (
            idEntry.get(),
            nameEntry.get(),
            emailEntry.get(),
            phoneEntry.get(),
            addressEntry.get(),
            genderEntry.get(),
            dobEntry.get()
        ))
        studentTable.delete(*studentTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('', END, values=data)

    search_window = Toplevel()
    search_window.title('Search Student')
    search_window.grab_set()
    search_window.resizable(False, False)

    idLabel = Label(search_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(search_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(search_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(search_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    dobLabel = Label(search_window, text='DOB', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=5, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=6, column=1, pady=15, padx=10)

    search_student_button = ttk.Button(search_window, text='SEARCH', command=search_data)
    search_student_button.grid(row=7, columnspan=2, pady=15)


def add_student():
    def add_data():
        if idEntry.get()==''or nameEntry=='' or phoneEntry.get()=='' or emailEntry.get()==''or genderEntry.get()=='' or dobEntry.get()=='' or addressEntry.get()=='':

            messagebox.showerror('error','all fields are required')
        else:
            currentdate = time.strftime('%d/%m/%y')
            currenttime = time.strftime('%H:%M:%S')
            try:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime))
                con.commit()
                result=messagebox.askyesno('confirm','data added succesfully do u want to clean the from?',parent=add_window)
                if result:
                    idEntry.delete(0,END)
                    nameEntry.delete(0, END)
                    phoneEntry.delete(0, END)
                    emailEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    genderEntry.delete(0, END)
                    dobEntry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('error','id cannot be repeated',parent=add_window)
                return

            query='select *from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                    studentTable.insert('',END,values=datalist)



    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(False,False)
    idLabel=Label(add_window,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel = Label(add_window, text='name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15,sticky=W)
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(add_window, text='phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15,sticky=W)
    phoneEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(add_window, text='email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15,sticky=W)
    emailEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(add_window, text='address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15,sticky=W)
    addressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    dobLabel = Label(add_window, text='dob', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=5, column=0, padx=30, pady=15,sticky=W)
    dobEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=5, column=1, pady=15, padx=10)

    genderLabel = Label(add_window, text='gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=6, column=1, pady=15, padx=10)


    add_student_button= ttk.Button(add_window,text='ADD STUDENT',command=add_data)
    add_student_button.grid(row=7,columnspan=2,pady=15)
def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host=hostEntry.get(),user=usernameEntry.get(),password=passwordEntry.get())
            mycursor=con.cursor()
            messagebox.showinfo('Success','Database connection successful',parent=connectWindow)
        except:


            messagebox.showerror('Error','Invalid details ',parent=connectWindow)
            return
        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query='create table student(id int not null primary key,name varchar(30),mobile varchar(10),email varchar(30),address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database connection successful', parent=connectWindow)
        connectWindow.destroy()

        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        exitstudentButton.config(state=NORMAL)



    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database connnection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='HOST NAME',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='USER NAME', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='PASSWORD', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)
count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(100,slider)

def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'Date:{date} \n Time: {currenttime}')
    datetimeLabel.after(1000,clock)
#GUI part
root=ttkthemes.ThemedTk()
root.set_theme('radiance')
root.geometry('1174x680+0+0')
root.resizable(0,0)
root.title('STUDENT MANAGEMENT SYSTEM')
datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Management System'
sliderLabel=Label(root,text=s,font=('times new roman',28,'bold'))
sliderLabel.place(x=200,y=0)
slider()
connectButton=ttk.Button(root,text='connect to database',command=connect_database)
connectButton.place(x=980,y=0)
leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)
logo_image=PhotoImage(file='students.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)
addstudentButton=ttk.Button(leftFrame,text='ADD STUDENT',width=25,state=DISABLED,command=add_student)
addstudentButton.grid(row=1,column=0,pady=20)
searchstudentButton=ttk.Button(leftFrame,text='SEARCH STUDENT',width=25,state=DISABLED,command=search_student)
searchstudentButton.grid(row=2,column=0,pady=20)
deletestudentButton=ttk.Button(leftFrame,text='DELETE STUDENT',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)
updatestudentButton=ttk.Button(leftFrame,text='UPDATE STUDENT',width=25,state=DISABLED,command=update_student)
updatestudentButton.grid(row=4,column=0,pady=20)
showstudentButton=ttk.Button(leftFrame,text='SHOW STUDENT',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)
exportstudentButton=ttk.Button(leftFrame,text='EXPORT STUDENT',width=25,state=DISABLED)
exportstudentButton.grid(row=6,column=0,pady=20)
exitstudentButton=ttk.Button(leftFrame,text='EXIT STUDENT',width=25,state=DISABLED,command=exit_student)
exitstudentButton.grid(row=7,column=0,pady=20)
rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)
scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)
studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email','Address','Gender','dob','added date','added time'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)
scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)
studentTable.pack(fill=BOTH,expand=1)
studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='name')
studentTable.heading('Mobile',text='mobile')
studentTable.heading('Email',text='email')
studentTable.heading('Address',text='address')
studentTable.heading('Gender',text='gender')
studentTable.heading('dob',text='dob')
studentTable.heading('added date',text='added date')
studentTable.heading('added time',text='added time')
studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Mobile',width=200,anchor=CENTER)
studentTable.column('Email',width=400,anchor=CENTER)
studentTable.column('Address',width=400,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('dob',width=100,anchor=CENTER)
studentTable.column('added date',width=200,anchor=CENTER)
studentTable.column('added time',width=200,anchor=CENTER)
style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',15,'bold'),foreground='red4',fieldbackground='white')
style.configure('Treeview.Heading',font=('arial',14,'bold'))
studentTable.config(show='headings')
root.mainloop()
