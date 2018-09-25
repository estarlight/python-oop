from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index ():
    return "Playground Rules"

@app.route('/play')
def blueBox ():
    return render_template('level1.html')

@app.route('/play/<x>')
def numBox (x):
    x = int(x)
    return render_template('level2.html', num = x)

@app.route('/play/<x>/<color>')
def colorBox (x,color):
    x = int(x)
    return render_template('level3.html', num = x, boxcolor = color)





if __name__=="__main__":
    app.run(debug=True)