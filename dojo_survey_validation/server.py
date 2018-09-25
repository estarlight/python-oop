from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'asdfadsfasdf'


@app.route('/')
def postForm():
    if not '_flashes' in session.keys():
        session.clear()
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def collectInfo ():

    session['comment'] = request.form['comment']
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session ['location'] = request.form['location']
    session['language'] = request.form['fav_language']

    if len(request.form['name']) < 1:
        flash("Name cannot be empty!",'name')
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!",'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address!", 'email')
    if len(request.form['comment']) > 120:
        # session['comment'] = request.form['comment']
        flash("Comment cannot be longer that 120 characters.",'comment')
    

    print(request.form)
    print("name:", request.form['name'])
    print("email:", request.form['email'])
    print("location:", request.form['location'])
    print("favorite language:", request.form['fav_language'])

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return render_template('result.html')


@app.route('/danger')
def dangerRedirect():
    print("A user tried to visit /danger. We have redirected the user to /")
    
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True) 