from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
import random

@app.route('/')
def home ():
    x = (random.randrange(0,101))
    print(x)
    session['answer'] = x

    return render_template('index.html')

@app.route('/guess',methods=["POST"])
def compareGuess():

    if int(request.form['guess']) < session['answer']:
        show_hint = "Too Low!"
    if int(request.form['guess']) > session['answer']:
        show_hint = "Too High!"
    if int(request.form['guess']) == session['answer']:
        return redirect('/correct_guess')

    else:
        return render_template('index.html', hint = show_hint)


@app.route('/correct_guess', methods=['GET'])
def correctGuess():
    show_hint = str(session['answer']) + " was the number!"
    return render_template('correct_guess.html', hint = show_hint)











if __name__=="__main__":
    app.run(debug=True) 