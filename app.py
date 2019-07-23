import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


#if __name__ == '__main__':
#    app.run(host='0.0.0.0', debug=True)

if __name__ == '__main__':
    from os import environ
    app.run(debug=False, host='0.0.0.0',port=environ.get("PORT", 5000))    
  

# test code c