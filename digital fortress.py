 #DIGITAL FORTRESS
import Tkinter as tkinter
import crypto
import sender
userhandle=''
password=''
receiverguy=''
key=''
message=''
incoming=''
inco=''
############################################################################################
userhandler=tkinter.Tk()
userhandler.title('user handle creator')
label1=tkinter.Label(userhandler,text='enter email below').pack()
user=tkinter.Entry(userhandler)
user.pack()
label2=tkinter.Label(userhandler,text='enter password below').pack()
passw=tkinter.Entry(userhandler,show='*')
passw.pack()

def getter():
        global userhandle,password
        userhandle=user.get()
        password=passw.get()
        if userhandle=='' or password=='':
                error=tkinter.Tk()
                error.title('error')
                label=tkinter.Label(error,text='enter valid email ID and password').pack()
                error.mainloop()
                
        else:
                userhandler.destroy()
submit=tkinter.Button(userhandler,text='click to submit',command=getter).pack()
userhandler.mainloop()
############################################################################################
keysetter=tkinter.Tk()
keysetter.title('keysetter')
label=tkinter.Label(keysetter,text='enter key below').pack()
keyt=tkinter.Entry(keysetter)
keyt.pack()
def getter():
        global key,userhandle,password
        key=keyt.get()
        if userhandle=='' or password=='':
                error=tkinter.Tk()
                error.title('error')
                label=tkinter.Label(error,text='you need to sign-in first!').pack()
                error.mainloop()

        else:
                if key=='':
                                error=tkinter.Tk()
                                error.title('error')
                                label=tkinter.Label(error,text='we need a key!....we do not encrypt using black magic').pack()
                                error.mainloop()
                else:
                        keysetter.destroy()
submit=tkinter.Button(keysetter,text='click to submit',command=getter).pack()
keysetter.mainloop()
############################################################################################
messager=tkinter.Tk()
messager.title('messager')
label1=tkinter.Label(messager,text='enter the email id of the recipient below').pack()
to=tkinter.Entry(messager)
to.pack()
label2=tkinter.Label(messager,text='enter message below').pack()
messaget=tkinter.Entry(messager)
messaget.pack()
def getter():
        global message,userhandle,password,key
        message=messaget.get().lower()
        receiverguy=to.get()
        if userhandle=='' or password=='':
                error=tkinter.Tk()
                error.title('error')
                label=tkinter.Label(error,text='you need to sign-in first').pack()
                error.mainloop()
        
        elif key=='':
                error=tkinter.Tk()
                error.title('error')
                label=tkinter.Label(error,text='we need a key!....we do not encrypt using black magic').pack()
                error.mainloop()
                
        
        elif message=='':
                error=tkinter.Tk()
                error.title('error')
                label=tkinter.Label(error,text='we do not read minds...we need the message!!').pack()
                error.mainloop()
        else:
                messager.destroy()
                mess=crypto.encrypt(message,key,userhandle)
                sender.sendmessage(userhandle,password,receiverguy,mess)
        

        
submitt=tkinter.Button(messager,text='click to send',command=getter).pack()
messager.mainloop()

############################################################################################
def display(incoming):
        def quitt():
                checkers.destroy()
                checker.destroy()
        checkers=tkinter.Tk()
        checkers.title('message found')
        lab2=tkinter.Label(checkers,text=str(incoming+'')).pack()
        but1=tkinter.Button(checkers,text='ok',command=quitt).pack()
        checkers.mainloop()
checker=tkinter.Tk()
checker.title('enter message')
lab1=tkinter.Label(checker,text='Enter text from email below').pack()
ent1=tkinter.Entry(checker)
ent1.pack()
def getter():
        global inco
        inco=ent1.get()
        display(crypto.decrypt(inco))
but1=tkinter.Button(checker,text='submit',command=getter).pack()
checker.mainloop()
'''

def quitter1():
        signinwindow.destroy()
signinwindow=tkinter.Tk()
signinwindow.title("DIGITAL FORTRESS")
signinwindow.geometry('300x160')        
label=tkinter.Label(signinwindow,text='welcome to the digital fortress\nOnly for Gmail\nplease sign in').pack()
but1=tkinter.Button(signinwindow,text='press to sign-in',command=userhandlemaker).pack()
but2=tkinter.Button(signinwindow,text='press to set a key',command=keyset).pack()
but3=tkinter.Button(signinwindow,text='press to send a message',command=message).pack()
but4=tkinter.Button(signinwindow,text='press to check for messages',command=checker).pack()
but5=tkinter.Button(signinwindow,text='QUIT',command=quitter1).pack()
mainwindow.mainloop()'''
