from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def home():
    
    if 'count' in session:
        session['count'] += 1
    else: session['count'] = 1
    
    if session['count'] == 1:
        visits = "visit"
    else: visits = "visits"
    
    print(session)
    

    return render_template('index.html', number = session['count'], visits = visits)

@app.route('/hidden', methods=['POST'])
def hidden():
    print(request.form)

    if request.form['count'] == "1":
        session['count'] +=1
    if request.form['count'] == "0":
        session['count'] = 0

    return redirect('/')





if __name__=="__main__":
    app.run(debug=True) 