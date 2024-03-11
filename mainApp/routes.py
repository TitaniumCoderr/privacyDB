from mainApp import app
from flask import render_template,request,flash,redirect,url_for
from mainApp.forms import checkLeakForm
import mysql.connector 
import hashlib

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
        found = checkDB(email, passwrd)
        if found==1:
            flash("found")
        else:
            flash("Not found")
    
    
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
    mycursor.execute(sql,val)
    rowcount=mycursor.rowcount

    mycursor.close()
    mydb.close()

    return rowcount

