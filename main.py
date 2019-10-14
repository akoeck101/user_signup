from flask import Flask, request, redirect, render_template, url_for
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/",methods=['post','get'])
def index():
    username=''
    password=''
    email=''
    username_error=""
    password_error =""
    email_error=""

    if request.method == 'GET':
        
        return render_template('index.html')

    else:
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email = request.form.get('email')
        
        
        if username == '':
           
            username_error="Please enter a username."
        elif len(username)>20 or len(username)<3:
            username_error="Please enter a valid username of 3 or more characters and less than 20 characters."
        if password == '':
            password_error="Please enter a password."
        elif confirm_password != password:
            password_error = "Passwords do not match."
        if len(email)>20 or len(email)<3:
            email_error = "Please enter a valid email of 3 or more characters and less than 20 characters."

        if username_error != "" or password_error != "":
            return render_template('index.html',email=email,username=username,username_error=username_error, password_error=password_error,email_error=email_error)
    
        
        return redirect(url_for('welcome', username=username))




@app.route("/welcome/<username>/")
def welcome(username):
    return render_template('welcome.html', username= username)


if __name__ == "__main__":
    app.run()


