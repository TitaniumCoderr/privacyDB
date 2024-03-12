from mainApp import app
from flask import render_template,request,flash,redirect,url_for
from mainApp.forms import checkLeakForm
import mysql.connector 
import hashlib
import time

def hash_value(value):
    sha256 = hashlib.sha384()
    sha256.update(value.encode())
    return sha256.hexdigest()

@app.route('/',methods=['GET','POST'])
def home():
    #create fomr object
    form =checkLeakForm()
    #if the form is submitted
    
    if request.method=="POST":
        email = hash_value(form.email.data)
        passwrd = hash_value(form.passwrd.data)
        found,time = checkDB(email, passwrd)
        time= round(time,3)
        if found==1:
            flash("found")
            flash(str(time))
        else:
            flash("Not found")
            flash(str(time))
    
    
    return render_template('home.html',form=form)

def checkDB(email, passwrd):
    mydb= mysql.connector.connect(
        host='localhost',
        user='uniadmin',
        password='password123',
        database='privacyDB'
    )
    #cursor object 
    
    mycursor=mydb.cursor(buffered=True)
    
    sql= "select email,password from users where email= %s and password=%s limit 1"
    val=(email,passwrd)
    start=time.time()
    mycursor.execute(sql,val)
    end=time.time()
    rowcount=mycursor.rowcount

    mycursor.close()
    mydb.close()

    return [rowcount,end-start]

