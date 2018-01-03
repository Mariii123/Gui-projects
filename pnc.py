from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("600x600+0+0")
root.title("Permutation & Combination Generator")
tf=Frame(root,width=800,height=50,bd=8,relief="raise")
tf.pack(side=TOP)
bf=Frame(root,width=800,height=50,bd=8,relief="raise")
bf.pack(side=LEFT)
var=IntVar()
fn=IntVar()
sn=IntVar()
ans=DoubleVar()
title=Label(tf,font=("arial",20,"bold"),fg="red",text="Permutation & Combination Generator")
title.grid()
def number(n):
    if n==0:
        return 1
    else:
        return number(n-1)*n
def combi(r):
    if r==0:
        return 1
    else:
        return number(r-1)*r
def diff(c):
    if c==0:
        return 1
    else:
        return number(c-1)*c
def answer():
    if var.get()==2:
        n=fn.get()
        r=sn.get()
        c=n-r
        a=number(n)
        b=combi(r)
        f=diff(c)
        d=b*f
        e=a/d
        ans.set(e)

    elif var.get()==1:
        n=fn.get()
        r=sn.get()
        c=n-r
        a=number(n)
        b=combi(r)
        f=diff(c)
        d=a/f
        ans.set(d)
def close():
    qexit=messagebox.askyesno("System","Confirm Exit")
    if qexit>0:
        root.destroy()
        return
def reset():
    fn.set("0")
    sn.set("0")
    ans.set("0")
l1=Label(bf,font=("arial",20,"bold"),text="Enter n",fg="blue",bd=8).grid(row=1)
l2=Label(bf,font=("arial",20,"bold"),text="Enter r",fg="blue",bd=8).grid(row=1,column=1)
l3=Label(bf,font=("arial",20,"bold"),text="Answer",fg="blue",bd=8).grid(row=3,padx=16,pady=16,sticky=E)
r1=Radiobutton(bf,font=("arial",20,"bold"),text="Permutation",fg="green",value=1,variable=var).grid(row=0,column=0,padx=16,pady=16)
r2=Radiobutton(bf,font=("arial",20,"bold"),text="Combination",fg="green",value=2,variable=var).grid(row=0,column=1,padx=16,pady=16)
e1=Entry(bf,font=("arial",20,"bold"),width=15,bd=8,textvariable=fn,fg="red").grid(row=2,column=0,padx=16,pady=16)
e2=Entry(bf,font=("arial",20,"bold"),width=15,bd=8,textvariable=sn,fg="red").grid(row=2,column=1,padx=16,pady=16)
e3=Entry(bf,font=("arial",20,"bold"),width=15,bd=8,textvariable=ans,fg="red").grid(row=4,column=0,columnspan=4,padx=16,pady=16)
b1=Button(bf,text="Result",font=("arial",20,"bold"),fg="green",width=15,bg="powder blue",command=answer).grid(row=5,column=0,padx=16,pady=16)
b2=Button(bf,text="Exit",font=("arial",20,"bold"),fg="red",width=15,bg="powder blue",command=close).grid(row=6,padx=16,pady=16)
b3=Button(bf,text="Reset",font=("arial",20,"bold"),fg="blue",width=15,bg="powder blue",command=reset).grid(row=5,column=1,padx=16,pady=16)
root.mainloop()
