import webbrowser
from Tkinter import *
paswd=Tk()
#Toplevel.transient(1)
icon=PhotoImage(file='image/icon.gif')
paswd.overrideredirect(1)
count=0
paswd.title("log on")#PROJECT NAME
def forget():
    webbrowser.open("192.168.4.2")
def clear1(self):
    username.delete(0,END)
def clear2(self):
    key.delete(0,END)
def check(self):
    if(username.get()=='123' and key.get()=='123'):
        pas=Label(paswd,text='correct password')
        pas.after('500',paswd.destroy)
        return 0
    else:
        global count
        pas=Label(paswd,text='wrong password \ usename ')
        pas.grid(pady=5,row=5)
        #print count
        count+=1
        if(count==3):
            Label(paswd,text='No more \n Attempt left',font='Impact 8 ').grid(pady=5,row=4)
            Button(paswd,text='forget password-:click here',width=30,command=forget).grid(row=5,columnspan=2)
            Label(paswd,text='OK',width=5).Button(paswd,text='OK').grid(pady=5,row=5,stick=W,padx=15)
def check1():
    if(username.get()=='123' and key.get()=='123'):
        pas=Label(paswd,text='correct password')
        pas.after('500',paswd.destroy)
        return 0
    else:
        global count
        pas=Label(paswd,text='wrong password \ username')
        pas.grid(pady=5,row=5)
        #print count
        count+=1
        if(count==3):
            Label(paswd,text='No more \n Attempt left',font='Impact 8 ').grid(pady=5,row=4)
            Button(paswd,text='forget password-:click here',width=30,command=forget).grid(row=5,columnspan=2)
            Label(paswd,text='OK',width=5).grid(pady=5,row=4,stick=W,padx=15)
def exi():
    raise SystemExit('Unauthorized login attempt')
Label(paswd,text='WELCOME TO LIFELINE DATABASE',font='Broadway 11 underline',image=icon,compound=LEFT).grid(stick=N+W+E+S,pady=5,padx=10)
Label(paswd,text='Username',font='Broadway 10').grid(row=2,column=0,stick=W,padx=10)
username=Entry(paswd)
username.bind('<Button>',clear1)
username.grid(row=2,column=0,stick=E,padx=10)
Label(paswd,text='Password',font='Broadway 10').grid(row=3,column=0,stick=W,padx=10)
key=Entry(paswd,show = '*')
key.bind('<Button>',clear2)
key.grid(pady=5,row=3,column=0,stick=E,padx=10)
variable=StringVar()
variable.set('User')
#Label(paswd,text='Type of user',font='Broadway 10').grid(row=4,column=0,stick=W,padx=10)
#OptionMenu(paswd,variable,'Admin','User').grid(row=4,column=0,sticky=E,padx=10)
Button(paswd,text='OK',command=check1,width=5).grid(pady=5,row=4,stick=W,padx=15)
Button(paswd,text='Quit',command=exi,width=5).grid(pady=5,row=4,stick=E,padx=15)
paswd.mainloop()
