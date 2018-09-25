from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
import random

@app.route('/')
def home():
    if 'gold_amount' in session:
        pass
    else: session['gold_amount'] = 0
    
    if not 'activities' in session:
        session['activities'] = []
    else: pass
    
    
    return render_template('index.html', gold = session['gold_amount'], activities = session['activities'])

@app.route('/process_money', methods=['POST'])
def processGold():
    
    if request.form['building'] == 'farm':
        x = (random.randrange(10,20))
        session['gold_amount'] += x
        print(x)
        print(session['gold_amount'])
    
    if request.form['building'] == 'cave':
        x = (random.randrange(5,10))
        session['gold_amount'] += x
        print(x)
        print(session['gold_amount'])

    if request.form['building'] == 'house':
        x = (random.randrange(2,5))
        session['gold_amount'] += x
        print(x)
        print(session['gold_amount'])
    
    if request.form['building'] == 'casino':
        x = (random.randrange(-50,50))
        session['gold_amount'] += x
        print(x)
        print(session['gold_amount'])
    
    if x > 0:
        new_dict = {
            'message': 'You won {} gold!'.format(x),
            'type': 'win'
        }
        session['activities'].append(new_dict)
    else:
        new_dict = {
            'message': 'You lost {} gold!'.format(x),
            'type': 'lose'
        }
        session['activities'].append(new_dict)

    return redirect('/')





if __name__=="__main__":
    app.run(debug=True) 