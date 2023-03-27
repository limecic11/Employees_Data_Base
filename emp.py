import pyfiglet
import sqlite3
print (pyfiglet.figlet_format("Emp   DB"))
print ("Enter The Number of Emps do you want==>")
no=int(input())
i=1
while(i<=no):
    i+=1
    name=input("Enter the Name")
    id=int(input("Enter the ID"))
    dep=input("Enter The Department")
    try:
        db=sqlite3.connect("app.db")
        db.execute("CREATE TABLE IF NOT EXISTS emp(id INTEGER,name TEXT,dep TEXT)")
        cr=db.cursor()
        cr.execute(f"insert into emp(id,name,dep) values ('{id}','{name}','{dep}')")
        db.commit()
        db.close()
    except:
        print("Error")