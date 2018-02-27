from tkinter import *
import tkinter.messagebox as messagebox
import random,time,sqlite3
import time
counter=1
conn=sqlite3.connect('prodatabase.db')
c=conn.cursor()
root=Tk()
root.title("Ice Cream Billing System")
root.geometry('1300x750+0+0')
rimg=PhotoImage(file="reset.png")
iimg=PhotoImage(file="info.png")
qimg=PhotoImage(file="close.png")
himg=PhotoImage(file="home.png")
bimg=PhotoImage(file="bill.png")
seimg=PhotoImage(file='search.png')
root.iconbitmap('logo.png')
def bills():
   root.withdraw()
   billing=Toplevel()
   billing.title("Ice Cream Billing system")
   billing.geometry("1300x750+0+0")
   tf=Frame(billing,width=900,height=75,relief='ridge',bd=10)
   tf.place(x=0,y=0)
   lf=Frame(billing,width=900,height=625,relief="ridge",bd=10)
   lf.place(x=0,y=100)
   lf1a=Frame(lf,width=450,height=500,relief="ridge",bd=10)
   lf1a.place(x=0,y=10)
   lf1b=Frame(lf,width=450,height=500,relief="ridge",bd=10)
   lf1b.place(x=450,y=10)
   lf2a=Frame(lf,width=450,height=125,relief="ridge",bd=10)
   lf2a.place(x=25,y=425)
   lf2b=Frame(lf,width=450,height=125,relief="ridge",bd=10)
   lf2b.place(x=475,y=425)
   rf=Frame(billing,width=400,height=750,relief="ridge",bd=10)
   rf.place(x=900,y=0)
   rf1=Frame(rf,width=400,height=75,relief="ridge",bd=10)
   rf1.place(x=0,y=0)
   rf2=Frame(rf,width=400,height=525,relief="ridge",bd=10)
   rf2.place(x=0,y=50)
   rf3=Frame(rf,width=400,height=250,relief="ridge",bd=10)
   rf3.place(x=0,y=520)
   def create_table():
       c.execute("CREATE TABLE IF NOT EXISTS bdata(bill_no INTEGER,chocobar INTEGER,strawberry INTEGER,vanilla INTEGER,butterscotch INTEGER,kulfi INTEGER,ice_cream_cake INTEGER,mint_ice INTEGER,cone_ice INTEGER,cup_ice INTEGER,mango_bar INTEGER,sub_total INTEGER,service_charge REAL,tax REAL,amount REAL)")
       conn.commit()
   def insert(bno,chocobar,strawberry,vanilla,butterscotch,kulfi,icecake,mintice,coneice,cupice,mangobar,subtotal,sc,tax,cost):
       c.execute("INSERT INTO bdata(bill_no ,chocobar,strawberry,vanilla,butterscotch,kulfi,ice_cream_cake,mint_ice,cup_ice,cone_ice,mango_bar,sub_total,service_charge,tax,amount) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(bno,chocobar,strawberry,vanilla,butterscotch,kulfi,icecake,mintice,coneice,cupice,mangobar,subtotal,sc,tax,cost))
       conn.commit()
   def bnogen():
      b=random.randint(1000,10000)
      return b
   def total():
      if (var1.get()>0 or var2.get()>0 or var3.get()>0 or var4.get()>0 or var5.get()>0 or var6.get()>0 or  var7.get()>0 or var8.get()>0 or var9.get()>0 or var10.get()>0) :
         try:
          e11.configure(state='normal')
          e11.configure(state='normal')
          e11.configure(state='normal')
          e11.configure(state='normal')
          subtot=var1.get()*10+var2.get()*20+var3.get()*20+var4.get()*30+var5.get()*15+var6.get()*75+var7.get()*50+var8.get()*40+var9.get()*30+var10.get()*35
          var11.set(subtot)
          gst=round(var1.get()*10*0.05+var2.get()*20*0.05+var3.get()*2*0.050+var4.get()*3*0.050+var5.get()*15*0.05+var6.get()*75*0.05+var7.get()*50*0.05+var8.get()*40*0.05+var9.get()*30*0.05+var10.get()*35*0.05,2)
          var13.set(gst)
          sc=round(subtot*0.06,2)
          var12.set(sc)
          tot=subtot+gst+sc
          t=round(tot,2)
          var14.set(t)
          e11.configure(state='disabled')
          e11.configure(state='disabled')
          e11.configure(state='disabled')
          e11.configure(state='disabled')
         except  Exception:
           e11.configure(state='disabled')
           reset()
           messagebox.showinfo('Error','Enter only Integer data')
      else:
         messagebox.showinfo('Missing','Enter Quantity')
   def reciept():
      if (var1.get()>0 or var2.get()>0 or var3.get()>0 or var4.get()>0 or var5.get()>0 or var6.get()>0 or  var7.get()>0 or var8.get()>0 or var9.get()>0 or var10.get()>0) and (var11.get()>0 and var12.get()>0 and var13.get()>0 and var14.get()>0) :
          global counter
          bno=bnogen()
          if counter :
              txt.configure(state='normal')
              txt.insert("1.0","\t A-Z IceCream \t \n ")
              txt.insert(END,"------------------------------------------------\n")
              txt.insert(END,"Bill no. \t \t" +str(bno)+"\n")
              txt.insert(END,"------------------------------------------------\n")
              txt.insert(END,"Item \t\tQty\tRate\n")
              txt.insert(END,"------------------------------------------------\n")
              txt.insert(END,"Chocobar \t \t" +str(var1.get())+"\t10 Rs/-\n \n")
              txt.insert(END,"Strawberry \t \t" +str(var2.get())+"\t20 Rs/- \n  \n")
              txt.insert(END,"Vanilla \t \t" +str(var3.get())+"\t20 Rs/- \n \n")
              txt.insert(END,"Butterscotch\t \t" +str(var4.get())+" \t30 Rs/-\n \n")
              txt.insert(END,"Kulfi \t \t" +str(var5.get())+"\t15 Rs/-\n \n")
              txt.insert(END,"Ice cream cake \t \t" +str(var6.get()) +"\t75 Rs/-\n \n")
              txt.insert(END,"Mint Ice cream \t \t" +str(var7.get())+"\t50 Rs/-\n \n")
              txt.insert(END,"Cone ice \t \t" +str(var8.get())+"\t40 Rs/-\n \n")
              txt.insert(END,"Cup ice \t \t" +str(var9.get())+"\t30 Rs/-\n \n")
              txt.insert(END,"Mango bar \t \t" +str(var10.get())+"\t35 Rs/-\n \n")
              txt.insert(END,"------------------------------------------------ \n \n")        
              txt.insert(END,"Sub total \t \t" +str(var11.get())+"\n \n")
              txt.insert(END,"GST \t \t" +str(var12.get())+"\n \n")
              txt.insert(END,"Tax \t \t" +str(var13.get())+"\n \n")
              txt.insert(END,"Total cost \t \t" +str(var14.get())+"\n \n")
              txt.insert(END,"\n\tThank You, Visit Again \t")
              txt.configure(state='disabled')
              counter=0
              y=messagebox.askyesno('Confirm','Do you want to save')
              if y>0:
                 create_table()
                 chocobar=var1.get()
                 strawberry=var2.get()
                 vanilla=var3.get()
                 butterscotch=var4.get()
                 kulfi=var5.get()
                 icecake=var6.get()
                 mintice=var7.get()
                 coneice=var8.get()
                 cupice=var9.get()
                 mangobar=var10.get()
                 subtotal=var11.get()
                 sc=var12.get()
                 tax=var13.get()
                 cost=var14.get()
                 insert(bno,chocobar,strawberry,vanilla,butterscotch,kulfi,icecake,mintice,coneice,cupice,mangobar,subtotal,sc,tax,cost)
                 time.sleep(0.01)
                 messagebox.showinfo('Success','Successfully Saved')
          else:
              messagebox.showinfo("Warning",'Reset First')
      else:
         messagebox.showerror('Error','Missing quantity or total')
   def goback():
      reset()
      root.deiconify()
      billing.withdraw()
   def quit():
       e=messagebox.askyesno("Billing System","Do you want to exit")
       if e>0:
           billing.destroy()
   def reset():
       global counter
       counter=1
       txt.configure(state='normal')
       var1.set("0")
       var2.set("0")
       var3.set("0")
       var4.set("0")
       var5.set("0")
       var6.set("0")
       var7.set("0")
       var8.set("0")
       var9.set("0")
       var10.set("0")
       var11.set("0.0")
       var12.set("0.0")
       var13.set("0.0")
       var14.set("0.0")
       txt.delete("1.0",END)
       txt.configure(state='disabled')
   title=Label(tf,font=("georgia",30,"bold"),fg="blue",text="                      A-Z   ICE-CREAMS                           ")
   title.pack(side=LEFT)
   typ1=Label(lf1a,text="Type",font=('georgia',20,'bold'),fg='blue')
   typ1.grid(row=0,column=0,padx=10,pady=10,sticky=W)
   qty1=Label(lf1a,text="Qty",font=('georgia',20,'bold'),fg='blue')
   qty1.grid(row=0,column=1,padx=10,pady=10,sticky=W)
   rate1=Label(lf1a,text="Rate",font=('georgia',20,'bold'),fg='blue')
   rate1.grid(row=0,column=2,padx=10,pady=10,sticky=W)
   l1=Label(lf1a,text="Chocobar",font=('Times New Roman',20,'bold'),fg='brown4')
   l1.grid(row=1,column=0,padx=10,pady=10,sticky=W)
   l2=Label(lf1a,text="Strawberry",font=('Times New Roman',20,'bold'),fg='red2')
   l2.grid(row=2,column=0,padx=10,pady=10,sticky=W)
   l3=Label(lf1a,text="Vanilla",font=('Times New Roman',20,'bold'),fg="yellow2")
   l3.grid(row=3,column=0,padx=10,pady=10,sticky=W)
   l4=Label(lf1a,text="Butterscotch",font=('Times New Roman',20,'bold'),fg='goldenrod1')
   l4.grid(row=4,column=0,padx=10,pady=10,sticky=W)
   l5=Label(lf1a,text="Icecream cake",font=('Times New Roman',20,'bold'),fg='green2')
   l5.grid(row=5,column=0,padx=10,pady=10,sticky=W)
   typ2=Label(lf1b,text="Type",font=('georgia',20,'bold'),fg='blue')
   typ2.grid(row=0,column=0,padx=10,pady=10,sticky=W)
   qty2=Label(lf1b,text="Qty",font=('georgia',20,'bold'),fg='blue')
   qty2.grid(row=0,column=1,padx=10,pady=10,sticky=W)
   rate2=Label(lf1b,text="Rate",font=('georgia',20,'bold'),fg='blue')
   rate2.grid(row=0,column=2,padx=10,pady=10,sticky=W)
   l6=Label(lf1b,text="Kulfi",font=('Times New Roman',20,'bold'),fg='magenta')
   l6.grid(row=1,column=0,padx=10,pady=10,sticky=W)
   l7=Label(lf1b,text="Mint Ice cream",font=('Times New Roman',20,'bold'),fg='green4')
   l7.grid(row=2,column=0,padx=10,pady=10,sticky=W)
   l8=Label(lf1b,text="Cone Ice",font=('Times New Roman',20,'bold'),fg='tan1')
   l8.grid(row=3,column=0,padx=10,pady=10,sticky=W)
   l9=Label(lf1b,text="Cup Ice",font=('Times New Roman',20,'bold'),fg='deep pink')
   l9.grid(row=4,column=0,padx=10,pady=10,sticky=W)
   l10=Label(lf1b,text="Mango bar",font=('Times New Roman',20,'bold'),fg='gold2')
   l10.grid(row=5,column=0,padx=10,pady=10,sticky=W)
   l11=Label(lf2a,text="Sub Total ",font=('georgia',20,'bold'),fg='blue4')
   l11.grid(row=0,column=0,padx=10,pady=10,sticky=W)
   l13=Label(lf2a,text="GST ",font=('georgia',20,'bold'),fg='blue4')
   l13.grid(row=1,column=0,padx=10,pady=10,sticky=W)
   l12=Label(lf2b,text="Tax",font=('georgia',20,'bold'),fg='blue4')
   l12.grid(row=0,column=0,padx=10,pady=10,sticky=W)
   l14=Label(lf2b,text="Total Cost",font=('georgia',20,'bold'),fg='blue4')
   l14.grid(row=1,column=0,padx=10,pady=10,sticky=W)
   l15=Label(lf2a,text="Rs/-",font=('Times New Roman',20,'bold'),fg='green2')
   l15.grid(row=0,column=2,pady=10,sticky=W)
   l16=Label(lf2a,text="Rs/-",font=('Times New Roman',20,'bold'),fg='green2')
   l16.grid(row=1,column=2,pady=10,sticky=W)
   l17=Label(lf2b,text="Rs/-",font=('Times New Roman',20,'bold'),fg='green2')
   l17.grid(row=0,column=2,pady=10,sticky=W)
   l18=Label(lf2b,text="Rs/-",font=('Times New Roman',20,'bold'),fg='green2')
   l18.grid(row=1,column=2,pady=10,sticky=W)
   l19=Label(rf1,text="Receipt",font=('georgia',20,'bold'),fg='blue4')
   l19.grid(row=0,column=0,padx=10,sticky=W)
   r1=Label(lf1a,text="10 Rs/-",font=('Times New Roman',20,'bold'),fg='brown2')
   r1.grid(row=1,column=2,padx=10,pady=10,sticky=W)
   r2=Label(lf1a,text="20 Rs/-",font=('Times New Roman',20,'bold'),fg='brown2')
   r2.grid(row=2,column=2,padx=10,pady=10,sticky=W)
   r3=Label(lf1a,text="20 Rs/-",font=('Times New Roman',20,'bold'),fg='brown2')
   r3.grid(row=3,column=2,padx=10,pady=10,sticky=W)
   r4=Label(lf1a,text="30 Rs/-",font=('Times New Roman',20,'bold'),fg='brown2')
   r4.grid(row=4,column=2,padx=10,pady=10,sticky=W)
   r5=Label(lf1a,text="75 Rs/-",font=('Times New Roman',20,'bold'),fg='brown2')
   r5.grid(row=5,column=2,padx=10,pady=10,sticky=W)
   r6=Label(lf1b,text="15 Rs/-",font=('Times New Roman',20,'bold'),fg='brown2')
   r6.grid(row=1,column=2,padx=10,pady=10,sticky=W)
   r7=Label(lf1b,text="50 Rs/-",font=('Times New Roman',20,'bold'),fg='brown2')
   r7.grid(row=2,column=2,padx=10,pady=10,sticky=W)
   r8=Label(lf1b,text="40 Rs/-",font=('Times New Roman',20,'bold'),fg='brown2')
   r8.grid(row=3,column=2,padx=10,pady=10,sticky=W)
   r9=Label(lf1b,text="30 Rs/-",font=('Times New Roman',20,'bold'),fg='brown2')
   r9.grid(row=4,column=2,padx=10,pady=10,sticky=W)
   r10=Label(lf1b,text="35 Rs/-",font=('Times New Roman',20,'bold'),fg='brown2')
   r10.grid(row=5,column=2,padx=10,pady=10,sticky=W)
   var1=IntVar()
   var2=IntVar()
   var3=IntVar()
   var4=IntVar()
   var5=IntVar()
   var6=IntVar()
   var7=IntVar()
   var8=IntVar()
   var9=IntVar()
   var10=IntVar()
   var11=DoubleVar()
   var12=DoubleVar()
   var13=DoubleVar()
   var14=DoubleVar()
   var15=IntVar()
   #===================Entries==========================
   e1=Entry(lf1a,font=('arial',20,'bold'),fg="black",width=5,bg='powder blue',textvariable=var1)
   e1.grid(row=1,column=1,sticky=E,padx=10,pady=10)
   e2=Entry(lf1a,font=('arial',20,'bold'),fg="black",bg='powder blue',width=5,textvariable=var2)
   e2.grid(row=2,column=1,sticky=E,padx=10,pady=10)
   e3=Entry(lf1a,font=('arial',20,'bold'),fg="black",bg='powder blue',width=5,textvariable=var3)
   e3.grid(row=3,column=1,sticky=E,padx=10,pady=10)
   e4=Entry(lf1a,font=('arial',20,'bold'),fg="black",bg='powder blue',width=5,textvariable=var4)
   e4.grid(row=4,column=1,sticky=E,padx=10,pady=10)
   e5=Entry(lf1a,font=('arial',20,'bold'),fg="black",bg='powder blue',width=5,textvariable=var5)
   e5.grid(row=5,column=1,sticky=E,padx=10,pady=10)
   e6=Entry(lf1b,font=('arial',20,'bold'),fg="black",bg='powder blue',width=5,textvariable=var6)
   e6.grid(row=1,column=1,sticky=E,padx=10,pady=10)
   e7=Entry(lf1b,font=('arial',20,'bold'),fg="black",bg='powder blue',width=5,textvariable=var7)
   e7.grid(row=2,column=1,sticky=E,padx=10,pady=10)
   e8=Entry(lf1b,font=('arial',20,'bold'),fg="black",bg='powder blue',width=5,textvariable=var8)
   e8.grid(row=3,column=1,sticky=E,padx=10,pady=10)
   e9=Entry(lf1b,font=('arial',20,'bold'),fg="black",bg='powder blue',width=5,textvariable=var9)
   e9.grid(row=4,column=1,sticky=E,padx=10,pady=10)
   e10=Entry(lf1b,font=('arial',20,'bold'),fg="black",bg='powder blue',width=5,textvariable=var10)
   e10.grid(row=5,column=1,sticky=E,padx=10,pady=10)
   e11=Entry(lf2a,font=('arial',20,'bold'),fg="black",bg='powder blue',width=7,textvariable=var11)
   e11.grid(row=0,column=1,sticky=E,padx=10,pady=10)
   e11.configure(state='disabled')
   e12=Entry(lf2a,font=('arial',20,'bold'),fg="black",bg='powder blue',width=7,textvariable=var12)
   e12.grid(row=1,column=1,sticky=E,padx=10,pady=10)
   e12.configure(state='disabled')
   e13=Entry(lf2b,font=('arial',20,'bold'),fg="black",bg='powder blue',width=7,textvariable=var13)
   e13.grid(row=0,column=1,sticky=E,padx=10,pady=10)
   e13.configure(state='disabled')
   e14=Entry(lf2b,font=('arial',20,'bold'),fg="black",bg='powder blue',width=7,textvariable=var14)
   e14.grid(row=1,column=1,sticky=E,padx=10,pady=10)
   e14.configure(state='disabled')
   #=================Textbox=================
   txt=Text(rf2,font=('georgia',12,'bold'),fg="purple",width=34,height=23)
   txt.grid(row=0,column=0)
   s=Scrollbar(rf2)
   s.grid(row=0,column=1,ipady=15)
   s.config(command=txt.yview)
   txt.configure(state='disabled',yscrollcommand=s.set)
   #=================buttons====================
   def b1a(event):
      b1['bg']='cyan'
   def b1b(event):
      b1['bg']='cyan2'
   def b2a(event):
      b2['bg']='cyan'
   def b2b(event):
      b2['bg']='cyan2'
   def b3a(event):
      b3['bg']='cyan'
   def b3b(event):
      b3['bg']='cyan2'
   def b4a(event):
      b4['bg']='cyan'
   def b4b(event):
      b4['bg']='cyan2'
   def b5a(event):
      b5['bg']='cyan'
   def b5b(event):
      b5['bg']='cyan2'
   b1=Button(rf3,text="Total",font=("georgia",15,'bold'),fg="black",cursor='hand2',bg='cyan2',relief='ridge',bd=8,command=total)
   b1.grid(row=0,column=0,padx=10,pady=10)
   b1.bind('<Enter>',b1a)
   b1.bind('<Leave>',b1b)
   b2=Button(rf3,text="Receipt",font=("georgia",15,'bold'),fg="black",cursor='hand2',bg='cyan2',relief='ridge',bd=8,command=reciept)
   b2.grid(row=0,column=1,padx=10,pady=10)
   b2.bind('<Enter>',b2a)
   b2.bind('<Leave>',b2b)
   b3=Button(rf3,text="Reset",font=("georgia",15,'bold'),fg="black",cursor='hand2',bg='cyan2',relief='ridge',bd=8,command=reset)
   b3.grid(row=0,column=2,padx=10,pady=10)
   b3.bind('<Enter>',b3a)
   b3.bind('<Leave>',b3b)
   b4=Button(rf3,text="Quit",font=("georgia",15,'bold'),fg="black",cursor='hand2',bg='cyan2',relief='ridge',bd=8,command=quit)
   b4.grid(row=1,column=1,padx=10,pady=10)
   b4.bind('<Enter>',b4a)
   b4.bind('<Leave>',b4b)
   b5=Button(rf3,text="Home",font=("georgia",15,'bold'),fg="black",cursor='hand2',bg='cyan2',relief='ridge',bd=8,command=goback)
   b5.grid(row=1,column=0,padx=10,pady=10)
   b5.bind('<Enter>',b5a)
   b5.bind('<Leave>',b5b)
   billing.mainloop()
def getinfo():
   root.withdraw()
   info=Toplevel()
   info.title("Ice Cream Billing System")
   info.geometry("1300x750+0+0")
   tf=Frame(info,width=700,height=60,relief='ridge',bd=10)
   tf.place(x=0,y=0)
   title=Label(tf,font=("georgia",30,"bold"),text="                        A-Z Ice-Creams                     ",fg="blue")
   title.pack()
   lf=Frame(info,width=800,height=600,relief='ridge',bd=10)
   lf.place(x=0,y=75)
   rf=Frame(info,width=495,height=670,relief='ridge',bd=10)
   rf.place(x=800,y=5)
   var15=IntVar()
   def back():
      info.withdraw()
      root.deiconify()
   def get():
       b=var15.get()
       txt.configure(state='normal')
       txt.delete('1.0',END)
       c.execute('SELECT * FROM bdata where bill_no='+str(b))
       d=c.fetchall()
       if len(d)>0:       
          for i in d:
              txt.insert("2.0","\t\tA-Z  IceCream \t\t \n \n")
              txt.insert(END,"------------------------------------------------------------\n")
              txt.insert(END,"Bill no. \t \t \t" +str(i[0])+"\n \n")
              txt.insert(END,"------------------------------------------------------------\n")
              txt.insert(END,"Item \t\t\tQty\tRate\n")
              txt.insert(END,"------------------------------------------------------------\n")
              txt.insert(END,"Chocobar \t \t \t" +str(i[1])+"\t 10 Rs/-\n \n")
              txt.insert(END,"Strawberry \t \t \t" +str(i[2])+"\t 20 Rs/-\n  \n")
              txt.insert(END,"Vanilla \t \t \t" +str(i[3])+"\t 20 Rs/- \n \n")
              txt.insert(END,"Butterscotch \t \t \t" +str(i[4])+"\t 30 Rs/- \n \n")
              txt.insert(END,"Kulfi \t \t \t"+str(i[5])+"\t 15 Rs/-\n \n")
              txt.insert(END,"Ice cream cake  \t \t \t" +str(i[6]) +"\t 75 Rs/-\n \n")
              txt.insert(END,"Mint Ice cream \t \t \t" +str(i[7])+"\t 50 Rs/-\n \n")
              txt.insert(END,"Cone ice \t \t \t" +str(i[8])+"\t 40 Rs/-\n \n")
              txt.insert(END,"Cup ice \t \t \t" +str(i[9])+"\t 30 Rs/-\n \n")
              txt.insert(END,"Mango bar \t \t \t" +str(i[10])+"\t 35 Rs/-\n \n ")
              txt.insert(END,"------------------------------------------------------------\n \n")
              txt.insert(END,"Sub total \t \t \t" +str(i[11])+"\n \n")
              txt.insert(END,"GST \t \t \t" +str(i[12])+"\n \n")
              txt.insert(END,"Tax \t \t \t" +str(i[13])+"\n \n")
              txt.insert(END,"Total cost \t \t \t" +str(i[14])+"\n \n")
              txt.configure(state='disabled')
       else:
         messagebox.showerror('Error','No such Bill number')            
   def delete():
         txt.configure(state='normal')
         txt.delete('1.0',END)
         var15.set("0")
         txt.configure(state='disabled')
   def f1(event):
      find['bg']='cyan'
      find['image']=seimg
      find['width']=215
      find['height']=180
      fi.place(x=80,y=67)
   def f2(event):     
      find['bg']="cyan2"
      find['text']='search'
      find['image']=''
      find['width']=15
      find['height']=7
      fi.place_forget()
   def r1(event):
      reset['bg']='cyan'
      reset['image']=rimg
      reset['width']=215
      reset['height']=180
      re.place(x=90,y=80)
   def r2(event):     
      reset['bg']="cyan2"
      reset['text']='Reset'
      reset['image']=''
      reset['width']=15
      reset['height']=7
      re.place_forget()
   def h1(event):
      home['bg']='cyan'
      home['image']=himg
      home['width']=215
      home['height']=180
      ho.place(x=90,y=65)
   def h2(event):     
      home['bg']="cyan2"
      home['text']='Home'
      home['image']=''
      home['width']=15
      home['height']=7
      ho.place_forget()
   def e1(event):
      ex['bg']='cyan'
      ex['image']=qimg
      ex['width']=215
      ex['height']=180
      e.place(x=93,y=52)
   def e2(event):     
      ex['bg']="cyan2"
      ex['text']='Exit'
      ex['image']=''
      ex['width']=15
      ex['height']=7
      e.place_forget()
   l1=Label(rf,text="Bill_no",font=('georgia',20,'bold'),relief='groove',bd=10,fg="blue")
   l1.place(x=5,y=5)
   e15=Entry(rf,font=('georgia',23,'bold'),fg="blue",relief='ridge',bd=10,width=7,textvariable=var15)
   e15.place(x=150,y=3)
   find=Button(lf,text="Search",bg='cyan2',font=('georgia',15,'bold'),width=15,height=7,relief='ridge',cursor='hand2',bd=10,fg='blue',command=get)
   find.place(x=50,y=50)
   find.bind('<Enter>',f1)
   find.bind('<Leave>',f2)
   fi=Label(find,text="Search",font=('georgia',7,'bold'),bg='cyan')
   fi.place_forget()
   reset=Button(lf,text="Reset",bg='cyan2',font=('georgia',15,'bold'),width=15,height=7,relief='ridge',cursor='hand2',bd=10,fg='blue',command=delete)
   reset.place(x=500,y=50)
   reset.bind('<Enter>',r1)
   reset.bind('<Leave>',r2)
   re=Label(reset,text="Reset",font=('georgia',7,'bold'),bg='cyan')
   re.place_forget()
   home=Button(lf,text="Home",bg='cyan2',font=('georgia',15,'bold'),width=15,height=7,relief='ridge',cursor='hand2',bd=10,fg='blue',command=back)
   home.place(x=50,y=300)
   home.bind('<Enter>',h1)
   home.bind('<Leave>',h2)
   ho=Label(home,text="Home",font=('georgia',7,'bold'),bg='cyan')
   ho.place_forget()
   ex=Button(lf,text="Exit",bg='cyan2',font=('georgia',15,'bold'),width=15,height=7,relief='ridge',bd=10,fg='blue',cursor='hand2',command=exit)
   ex.place(x=500,y=300)
   ex.bind('<Enter>',e1)
   ex.bind('<Leave>',e2)
   e=Label(ex,text="Exit",font=('georgia',7,'bold'),bg='cyan')
   e.place_forget()
   txt=Text(rf,font=('georgia',12,'bold'),fg="blue",relief='ridge',bd=10,width=43,height=31)
   s=Scrollbar(rf,relief='ridge',bd=10)
   s.place(x=430,y=300)
   s.config(command=txt.yview)
   txt.configure(yscrollcommand=s.set,state='disabled')
   txt.place(x=10,y=60)
def exit():
   e=messagebox.askyesno('Exit','Do you want to exit')
   if e>0:
      root.destroy()
def ug():
      root.withdraw()
      dox=Toplevel()
      logo=PhotoImage(file='mlogo.png')
      dox.geometry('280x440+0+0')
      dox.title('User Guide')
      def close():
         root.deiconify()
         dox.withdraw()
      def license():
         lic=Toplevel()
         txt=Text(lic)
         txt.insert(END,'Copyright (c) 2018 Marish Software Foundation. All Rights Reserved.')
         txt.pack()
         lic.mainloop()
      def credits():
         cre=Toplevel()
         txt=Text(cre)
         txt.insert(END,'Thanks to www.python-course.eu, tutorialspoint, and priyanka teacher for supporting ICBS development ')
         txt.pack()
         cre.mainloop()
      txtbox=Text(dox,font=('georgia',20,'bold'),relief='ridge',bd=10,bg='white',height=10)
      txtbox.image_create(END,image=logo)
      txtbox.insert(END,'ICBS \n \n')
      txtbox.configure(font=('georgia',10))
      txtbox.insert(END,"Marish's Ice Cream Billing System\n\n")
      txtbox.insert(END,'mail:marishwaran22@gmail.com\n\n')
      txtbox.configure(state='disabled')
      txtbox.pack()
      b1=Button(dox,text='Close',font=('georgia',15),relief='groove',command=close)
      b1.place(x=15,y=200)
      b2=Button(dox,text='License',font=('georgia',15),relief='groove',command=license)
      b2.place(x=90,y=200)
      b3=Button(dox,text='Credits',font=('georgia',15),relief='groove',command=credits)
      b3.place(x=185,y=200)
      dox.mainloop()
def billcolor1(event):
   billbtn['bg']="cyan"
   billbtn['image']=bimg
   billbtn['width']=483
   billbtn['height']=250
   l1.place(x=210,y=80)
   l1['bg']='cyan'
def billcolor2(event):
   billbtn['bg']="cyan2"
   billbtn['text']='Billing System'
   billbtn['image']=''
   billbtn['width']=40
   billbtn['height']=10
   l1.place_forget()
def reccolor1(event):
   recbtn['bg']="cyan"
   recbtn['image']=iimg
   recbtn['width']=483
   recbtn['height']=250
   l2.place(x=220,y=50)
   l2['bg']='cyan'
def reccolor2(event):
   recbtn['bg']="cyan2"
   recbtn['text']='Retreival System'
   recbtn['image']=''
   recbtn['width']=40
   recbtn['height']=10
   l2.place_forget()
def excolor1(event):
   ex['bg']="cyan2"
   ex['image']=''
   ex['text']='Exit'
   ex['width']=40
   ex['height']=5
   l3.place_forget()
def excolor2(event):
   ex['bg']='cyan'
   ex['image']=qimg
   ex['width']=483
   ex['height']=130
   l3.place(x=229,y=30)
   l3['bg']='cyan'
img=PhotoImage(file='mlogo.png')
top=Frame(root,width=1300,height=60,relief='ridge',bd=10)
top.place(x=0,y=0)
title=Label(top,font=("georgia",35,),text="                               ICE CREAM BILLING SYSTEM                         ",fg="blue")
title.pack()
top1=Frame(root,width=1200,height=60,relief='ridge',bd=8)
top1.place(x=450,y=100)
que=Label(top1,text="Which System you want to load ?",font=('georgia',20),fg='blue')
que.pack()
menubar=Menu(top1)
root.config(menu=menubar)
filemenu = Menu(menubar)
filemenu.add_command(label="User Guide",command=ug )
filemenu.add_separator()
filemenu.add_command(label="About",)
filemenu.add_separator()
menubar.add_cascade(label='Help ',menu=filemenu)
billbtn=Button(root,bg='cyan2',font=('georgia',15),cursor='hand2',text="Billing System",relief='ridge',bd=10,width=40,height=10,command=bills)
billbtn.place(x=60,y=200)
billbtn.bind('<Enter>',billcolor1)
billbtn.bind('<Leave>',billcolor2)
l1=Label(billbtn,font=('georgia',7,'bold'),text="Bill System",fg='black')
l1.place(x=224,y=238)
l1.place_forget()
recbtn=Button(root,bg='cyan2',font=('georgia',15),cursor='hand2',text="Retreival System",relief='ridge',bd=10,width=40,height=10,command=getinfo)
recbtn.place(x=740,y=200)
recbtn.bind('<Enter>',reccolor1)
recbtn.bind('<Leave>',reccolor2)
l2=Label(recbtn,font=('georgia',7,'bold'),text="Bill Info",fg='black')
l2.place(x=224,y=238)
l2.place_forget()
ex=Button(root,bg='cyan2',font=('georgia',15),cursor='hand2',text="Exit System",relief='ridge',bd=10,width=40,height=5,command=exit)
ex.place(x=400,y=500)
ex.bind('<Enter>',excolor2)
ex.bind('<Leave>',excolor1)
l3=Label(ex,font=('georgia',7,'bold'),text="Exit",fg='black')
l3.place(x=224,y=30)
l3.place_forget()
root.mainloop()
