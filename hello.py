from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return render_template('index.html')

@app.route('/good')
def good():
    name = "Good"
    return name

## おまじない
if __name__ == "__main__":
    app.run()
