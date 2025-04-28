from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Field Cannot Be Empty')
    elif usernameEntry.get()=='yashwanth' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error','Invalid Credentials')

window=Tk()
window.geometry('1280x700+0+0')
window.title('Login System ')
backgroundImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)
loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)
logoImage=PhotoImage(file='ul.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file='pr.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='USERNAME',compound=LEFT,font=('times new roman',20,'bold'))
usernameLabel.grid(row=1,column=0,pady=10,padx=20)
usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bg='white',bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)
passwordImage=PhotoImage(file='padlock.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='PASSWORD',compound=LEFT,font=('times new roman',20,'bold'))
passwordLabel.grid(row=2,column=0,pady=10,padx=20)
passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bg='white',bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)
loginButton=Button(loginFrame,text='LOGIN',font=('times new roman',15,'bold'),width=15,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)
window.mainloop()
