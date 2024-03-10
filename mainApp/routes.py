from mainApp import app
from flask import render_template,request,flash,redirect,url_for
from mainApp.forms import checkLeakForm
import mysql.connector 
import hashlib

@app.route('/',methods=['GET','POST'])
def home():
    #create fomr object
    form =checkLeakForm()
    #if the form is submitted
    if request.method=="POST":
        email=form.email.data
        passwrd=form.passwrd.data

        #hash user email
        sha256= hashlib.sha384()
        sha256.update(email.encode())
        email=sha256.hexdigest()

        #hash user password
        sha256= hashlib.sha384()
        sha256.update(passwrd.encode())
        passwrd=sha256.hexdigest()
        
        print(email,passwrd)

        return redirect(url_for("home"))
    
        


    return render_template('home.html',form=form)

def checkDB():
    mydb= mysql.connector.connect(
        host='localhost',
        user='uniadmin',
        password='password123',
        database='privacyDB'
    )
