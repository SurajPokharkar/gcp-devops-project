from flask import Flask
app = Flask(__name__)

# route point that is the base route of application.
@app.route('/')

# define function
def hello_world():
    return 'Hello, Simple Flask Application'