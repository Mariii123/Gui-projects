from tkinter import *
import tkinter.messagebox as msg
root=Tk()
click=True

def play(buttons):
    global click
    if (buttons["text"]=="" and click==True ):
        buttons["text"]="X"
        click=False
    if (  buttons["text"]=="" and click==False):
        buttons["text"]="O"
        click=True
    if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" or
        b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X" or
        b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X" or
        b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" or
        b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" or
        b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X" or
        b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X" or
        b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X" ):
        msg.showinfo("Winner X","X Wins")
    if (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" or
        b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O" or
        b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O" or
        b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" or
        b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" or
        b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O" or
        b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O" or
        b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O" ):
        buttons["fg"]="blue"
        msg.showinfo("Winner O","O Wins")
        
b1=Button(root,text="",bd=16,fg="blue",command=lambda:play(b1))
b1.grid(row=0,column=0)
b2=Button(root,text="",bd=16,fg="blue",command=lambda:play(b2))
b2.grid(row=0,column=1)
b3=Button(root,text="",bd=16,fg="blue",command=lambda:play(b3))
b3.grid(row=0,column=2)
b4=Button(root,text="",bd=16,fg="blue",command=lambda:play(b4))
b4.grid(row=1,column=0)
b5=Button(root,text="",bd=16,fg="blue",command=lambda:play(b5))
b5.grid(row=1,column=1)
b6=Button(root,text="",bd=16,fg="blue",command=lambda:play(b6))
b6.grid(row=1,column=2)
b7=Button(root,text="",bd=16,fg="blue",command=lambda:play(b7))
b7.grid(row=2,column=0)
b8=Button(root,text="",bd=16,fg="blue",command=lambda:play(b8))
b8.grid(row=2,column=1)
b9=Button(root,text="",bd=16,fg="blue",command=lambda:play(b9))
b9.grid(row=2,column=2)
root.mainloop()

        
    
