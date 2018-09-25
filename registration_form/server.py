from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'asdfadsfasdf'

@app.route('/')
def homePage():
    if not '_flashes' in session.keys():
        session.clear()

    return render_template('index.html')

@app.route('/validation', methods=['POST'])
def validate():

    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    

    if len(request.form['first_name']) < 1:
        flash("First name is required",'first_name')
    if len(request.form['last_name']) < 1:
        flash("Last name is required",'last_name')
    if len(request.form['email']) < 1:
        flash("Email is required",'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address!", 'email')

    if len(request.form['password']) < 1:
        flash("Password is required",'password')
    elif len(request.form['password']) < 9:
        flash("Password must be more than 8 characters", 'password')

    if len(request.form['confirm_password']) < 1:
        flash("Must confirm password",'confirm_password')
    if request.form['confirm_password'] == request.form['password']:
        pass
    else:
        flash("Password does not match", 'confirm_password')
    
    if not request.form['first_name'].isalpha():
        flash("First Name cannot contain numbers", 'first_name')
    if not request.form['last_name'].isalpha():
        flash("Last Name cannot contain numbers", 'first_name')
    
    print(session)

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return render_template('success.html')





if __name__=="__main__":
    app.run(debug=True) 