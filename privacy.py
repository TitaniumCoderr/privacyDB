import mysql.connector
import hashlib

#Establish connection with MySQL database 
mydb= mysql.connector.connect(
    host='localhost',
    user='uniadmin',
    password='password123',
    database='privacyDB'
)

#cursor object 
mycursor=mydb.cursor()


f=open('project1/credentials2.txt') 
lines=f.read().splitlines()

for line in lines:
    try:
        email,passwrd=line.split(':',1)
        sha256= hashlib.sha384()
        sha256.update(email.encode())
        hashemail=sha256.hexdigest()

        sha256= hashlib.sha384()
        sha256.update(passwrd.encode())
        hashpasswrd=sha256.hexdigest()

        sql='insert into users (email,password) values (%s,%s)'
        val=(hashemail,hashpasswrd)
        mycursor.execute(sql,val)

        mydb.commit()
        print(mycursor.rowcount, "record inserted.")


    except:
        email,passwrd=line.split(';',1)
        sha256= hashlib.sha384()
        sha256.update(email.encode())
        hashemail=sha256.hexdigest()

        sha256= hashlib.sha384()
        sha256.update(passwrd.encode())
        hashpasswrd=sha256.hexdigest()

        sql='insert into users (email,password) values (%s,%s)'
        val=(hashemail,hashpasswrd)
        mycursor.execute(sql,val)

        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

mycursor.close()
mydb.close()