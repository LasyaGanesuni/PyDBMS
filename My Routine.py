from tkinter import*
import mysql.connector
from functools import partial

def insert(a1,a2,a3,a4,a5,a6):
	b1=a1.get()
	b2=a2.get()
	b3=a3.get()
	b4=a4.get()
	b5=a5.get()
	b6=a6.get()
	mydb=mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="La$ya123",
			database="lydatabase"
		)
	mycursor= mydb.cursor()
	mycursor.execute("CREATE TABLE IF NOT EXISTS Routine (id INT AUTO_INCREMENT PRIMARY KEY, Date VARCHAR(255), Earnings VARCHAR(255), Exercise VARCHAR(255), Study VARCHAR(255),Diet VARCHAR(255), Python VARCHAR(255))")
	sql="INSERT INTO Routine (Date,Earnings,Exercise,Study,Diet,Python) VALUES (%s,%s,%s,%s,%s,%s)"
	val=(b1,b2,b3,b4,b5,b6)
	myresult=mycursor.execute(sql,val)
	mydb.commit()

	return myresult

def view():
	mydb=mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="La$ya123",
			database="lydatabase"
		)
	mycursor= mydb.cursor()
	mycursor.execute("SELECT * FROM Routine")
	myresult=mycursor.fetchall()
	mydb.commit()
	
	return myresult

def delete(id):
	mydb=mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="La$ya123",
			database="lydatabase"
		)
	mycursor= mydb.cursor()
	sql=("DELETE FROM Routine where id=%s")
	val=(id,)
	mycursor.execute(sql,val)
	mydb.commit()
	return

def search(a1='',a2='',a3='',a4='',a5='',a6=''):
	b1=a1.get()
	b2=a2.get()
	b3=a3.get()
	b4=a4.get()
	b5=a5.get()
	b6=a6.get()
	mydb=mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="La$ya123",
			database="lydatabase"
		)
	mycursor= mydb.cursor()
	sql=("SELECT * FROM Routine where Date=%s or Earnings=%s or Exercise=%s or Study=%s or Diet=%s or Python=%s")
	val=(b1,b2,b3,b4,b5,b6)
	mycursor.execute(sql,val)
	myresult=mycursor.fetchall()
	mydb.commit()
	return myresult

def view_command():
	list.delete(0,END)
	for row in view():
		list.insert(END,row)
	return

def search_command():
	list.delete(0,END)
	for row in search():
		list.insert(END,row)
	return

def add_command(a1,a2,a3,a4,a5,a6):
	insert(a1,a2,a3,a4,a5,a6)
	list.delete(0,END)
	list.insert(END,(a1.get(),a2.get(),a3.get(),a4.get(),a5.get(),a6.get()))
	return

def get_selected_row(event):
	global selected_row
	index=list.curselection()[0]
	selected_row=list.get(index)
	return
	

def delete_command():
	delete(selected_row[0])
	return

win=Tk()
win.title("MY ROUTINE DATABASE SYSTEM")

l1=Label(win,text='Date')
l1.grid(row=0,column=0)
l1=Label(win,text='Earnings')
l1.grid(row=0,column=2)
l1=Label(win,text='Exercise')
l1.grid(row=1,column=0)
l1=Label(win,text='Study')
l1.grid(row=1,column=2)
l1=Label(win,text='Diet')
l1.grid(row=2,column=0)
l1=Label(win,text='Python')
l1.grid(row=2,column=2)

date_text=StringVar()
e1=Entry(win,textvariable=date_text,bd=3)
e1.grid(row=0,column=1)

earnings_text=StringVar()
e2=Entry(win,textvariable=earnings_text,bd=3)
e2.grid(row=1,column=1)

exercise_text=StringVar()
e3=Entry(win,textvariable=exercise_text,bd=3)
e3.grid(row=2,column=1)

study_text=StringVar()
e4=Entry(win,textvariable=study_text,bd=3)
e4.grid(row=0,column=3)

diet_text=StringVar()
e5=Entry(win,textvariable=diet_text,bd=3)
e5.grid(row=1,column=3)

python_text=StringVar()
e6=Entry(win,textvariable=python_text,bd=3)
e6.grid(row=2,column=3)

l=Label(win)
l.grid(row=3,column=0)

list=Listbox(win,height=8,width=35,bd=5)
list.grid(row=4,column=0,rowspan=9,columnspan=2)

sb=Label(win)
sb.grid(row=4,column=2,rowspan=9)

list.bind('<<ListboxSelect>>',get_selected_row)

add_command=partial(add_command,date_text,earnings_text,exercise_text,study_text,diet_text,python_text)
search=partial(search,date_text,earnings_text,exercise_text,study_text,diet_text,python_text)


b1=Button(win,text='ADD',width=12,pady=5,command=add_command)
b1.grid(row=4,column=3)
b1=Button(win,text='Search',width=12,pady=5,command=search_command)
b1.grid(row=5,column=3)
b1=Button(win,text='Delete date',width=12,pady=5,command=delete_command)
b1.grid(row=6,column=3)
b1=Button(win,text='View all',width=12,pady=5,command=view_command)
b1.grid(row=7,column=3)
b1=Button(win,text='Close',width=12,pady=5,command=win.destroy)
b1.grid(row=8,column=3)

win.mainloop()