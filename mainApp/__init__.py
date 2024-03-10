from flask import Flask

app=Flask(__name__)
app.config['SECRET_KEY']='titanium_no_look'

from mainApp import routes
