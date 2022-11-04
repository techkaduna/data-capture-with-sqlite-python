from tkinter import *
import sqlite3

#setting up the window
droot = Tk()
#droot.iconbitmap("./favicon.ico")
droot.title("Data Base app")
#droot.geometry("500x650+300+300")
droot.resizable(0,0)

#creating the label
fName_label = Label(droot,text="First Name",font=("Bahnschrift Condensed",15))
fName_label.grid(row=0,column=0)

lName_label = Label(droot,text="Last Name",font=("Bahnschrift Condensed",15))
lName_label.grid(row=1,column=0)

add_label = Label(droot,text="Address",font=("Bahnschrift Condensed",15))
add_label.grid(row=2,column=0)

city_label = Label(droot,text="city",font=("Bahnschrift Condensed",15))
city_label.grid(row=3,column=0)

zip_label = Label(droot,text="ZIp code",font=("Bahnschrift Condensed",15))
zip_label.grid(row=4,column=0)

#defining the click function
def click():
    
    #creating sqlite connection // sinct the database is already created the content will be written on
    conn = sqlite3.connect("mydatabase.db")
    #creating cursor
    curs = conn.cursor()

    #insert input into table
    curs.execute("INSERT INTO ADDRESSES VALUES(:fname,:lname,:add,:city,:zipp)",
                {
                    "fname":fname.get(),
                    "lname":lname.get(),
                    "add":add.get(),
                    "city":city.get(),
                    "zipp":zipp.get()
                }
    )
    #commiting change to database
    conn.commit()
    #closing connection
    conn.close()
    

    #delete the inputs after submission
    fname.delete(0,END)
    lname.delete(0,END)
    add.delete(0,END)
    city.delete(0,END)
    zipp.delete(0,END)
#defining query button

#defining delete record function   
def delete():
    #creating sqlite connection // sinct the database is already created the content will be written on
    conn = sqlite3.connect("mydatabase.db")
    #creating cursor
    curs = conn.cursor()
    #Deleting record by OID
    sql = "DELETE FROM ADDRESSES WHERE oid = "+ delEntry.get()
    curs.execute(sql)
    #Create delete entry label
    deLabel = Label(droot,text="Student with OID: "+str(delEntry.get())+" deleted!",font=("CargoD",10))
    deLabel.grid(row=8,column=0)

    #commiting change to database
    conn.commit()
    #closing connection
    conn.close()

#defining clear label function
def clear():
    print(delEntry.get())
    

def query():
    #creating sqlite connection // sinct the database is already created the content will be written on
    conn = sqlite3.connect("mydatabase.db")
    #creating cursor
    curs = conn.cursor()
    #creating the query
    curs.execute("SELECT *,oid FROM ADDRESSES")
    records = curs.fetchall()

    prt_rec = " "
    for items in records:
        prt_rec += "Name: "+str(items[0])+" "+ str(items[1]) +"\t"+" OID:"+str(items[5])+"\n"

    #creating label widget that gets the items out
    
    q_label = Label(droot,text=prt_rec,font=("Bahnschrift",12))
    q_label.grid(row=7,column=0,columnspan=2,pady=(5,0))
    #commiting change to database
    conn.commit()
    #closing connection
    conn.close()

#Creating entry feilds
fname = Entry(droot,width=45)
fname.grid(row=0,column=1,ipadx=0,ipady=5)

lname = Entry(droot,width=45)
lname.grid(row=1,column=1,ipadx=0,ipady=5)


add = Entry(droot,width=45)
add.grid(row=2,column=1,ipadx=0,ipady=5)


city = Entry(droot,width=45)
city.grid(row=3,column=1,ipadx=0,ipady=5)


zipp = Entry(droot,width=45)
zipp.grid(row=4,column=1,ipadx=0,ipady=5)

#creating submit button
btn = Button(droot,text="SUBMIT",relief="flat",command=click)
btn.grid(row=5,column=0,columnspan=1,pady=10,padx=10,ipadx=10)
    
#creating the query button
btn = Button(droot,text="QUERY",relief="flat",command=query)
btn.grid(row=5,column=1,columnspan=1,pady=10,padx=10,ipadx=10)

#creating the clear button
btn = Button(droot,text="CLEAR",relief="flat",command=clear)
btn.grid(row=5,column=2,columnspan=1,pady=10,padx=10,ipadx=10)

#creating the delete from database button
btn = Button(droot,text="DELETE",relief="flat",command=delete)
btn.grid(row=6,column=0,columnspan=1,pady=10,padx=10,ipadx=10)

#create delete entry
delEntry = Entry(droot,width=25)
delEntry.grid(row=6,column=1,ipadx=0,ipady=5)


droot.mainloop()