from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])
def postInfo():
    print(request.form)
    print("Strawberry:", request.form['strawberry'])
    print("Raspberry:", request.form['raspberry'])
    print("Apple:", request.form['apple'])

    sum = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])

    return render_template('checkout.html', total = sum)




if __name__=="__main__":
    app.run(debug=True) 