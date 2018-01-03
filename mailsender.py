import smtplib

from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("Mail Sender")
root.geometry("700x400+0+0")
root.configure(bd=10,bg="black")
tf=Frame(root,width=600,height=30,relief="raise",bd=16)
tf.pack(side=TOP)
bf=Frame(root,width=700,height=350,relief="raise",bd=16)
bf.pack(side=TOP)
title=Label(tf,text="           Text   Mail   Sender          ",font=("arial",30,"bold"),fg="blue").pack()
txt=StringVar()
smail=StringVar()
spassword=StringVar()
rmail=StringVar()
def Exit():
    qexit=tkinter.messagebox.askyesno("Exit","Confirm Exit")
    if qexit>0:
        root.destroy()
        
def sendemail():
    try:
        msg=txt.get()
        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        a=smail.get()
        b=spassword.get()
        
        c=rmail.get()
        mail.login(a,b)
        mail.sendmail(a,c,msg)
    except Exception:
       tkinter.messagebox.showinfo("Error","Invalid Email address or Password")
    else:
        tkinter.messagebox.showinfo("Success","Message Sent Successfully")
        
sn=Label(bf,text="Sender",font=("arial",20,"bold"),fg="red").grid(row=0,column=0,sticky=W,padx=20)
pas=Label(bf,text="Password",font=("arial",20,"bold"),fg="red").grid(row=1,column=0,sticky=W,padx=20)
rn=Label(bf,text="Reciever",font=("arial",20,"bold"),fg="red").grid(row=2,column=0,sticky=W,padx=20)
rn=Label(bf,text="Message",font=("arial",20,"bold"),fg="red").grid(row=3,column=0,sticky=W,padx=20)
sm=Entry(bf,text="",font=("arial",15,"bold"),fg="blue",textvariable=smail).grid(row=0,column=1,sticky=W,ipadx=20)
pm=Entry(bf,text="",font=("arial",15,"bold"),fg="blue",textvariable=spassword,show='*').grid(row=1,column=1,sticky=W,ipadx=20)
rm=Entry(bf,text="",font=("arial",15,"bold"),fg="blue",textvariable=rmail).grid(row=2,column=1,sticky=W,ipadx=20)
me=Entry(bf,text="",font=("arial",15,"bold"),fg="blue",textvariable=txt).grid(row=3,column=1,ipady=40,ipadx=100,sticky=W)
b1=Button(bf,text="Send",font=("arial",15,"bold"),fg="blue",command=sendemail).grid(row=4,sticky=W)
b2=Button(bf,text="Exit",font=("arial",15,"bold"),fg="blue",command=Exit).grid(row=4,column=1,sticky=W)
root.mainloop()
