from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is homepage'
    

@app.route('/about')
def about():
    return 'This is about page'
