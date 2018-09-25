from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def postForm():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def collectInfo ():
    print("Got Post Info")
    print(request.form)
    print("name:", request.form['name'])
    print("email:", request.form['email'])
    print("location:", request.form['location'])
    print("favorite language:", request.form['fav_language'])

    return render_template('result.html')


@app.route('/danger')
def dangerRedirect():
    print("A user tried to visit /danger. We have redirected the user to /")
    
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True) 