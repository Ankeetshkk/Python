#======================================================Module import===============================================================================
from Tkinter import *
import tkMessageBox
# ----------------------------clear function----------------------------------------------
def clear1(self):
    key.delete(0,END)
def clear2(self):
    age.delete(0,END)
def clear3(self):
    mob.delete(0,END)
def clear4(self):
    suffer.delete(0,END)
def clear5(self):
    dr.delete(0,END)
def clear6(self):
    search.delete(0,END)
# ----------------------------Entry checker  function----------------------------------------------
def check(self):
    import p  
#==============================create setting  window===================================================================
master=Tk()
master.geometry('1000x150')
#root.bind('<Motion>',motion)
master.title('Setting Window')#setting window
#root.attributes('-fullscreen', True)
#==============IMAGE USED==================================================================================show='*'
src='image/header.gif'
icon= PhotoImage(file='image/icon.gif')
header=PhotoImage(file=src)
#bottom=PhotoImage(file='image/bottom.gif')
header1=PhotoImage(file='image/header1.gif')
search_box=PhotoImage(file='image/search.gif')
#root.call('wm', 'iconphoto', root._w, icon)

Label(master,text='______________________________________setting______________________________________',font='impact 15 bold').grid(row=2,column=0,columnspan=14,stick=W)
Label(master,text='--------------------------------------password--------------------------------------',font='impact 9 bold').grid(row=3,column=0,columnspan=7,stick=W)
Label(master,text='New password').grid()
pas=Entry(master,show ='*')
pas.bind('<Button>',check)
pas.grid()


master.mainloop()
