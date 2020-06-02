# from flask import Flask, render_template
# 
# app = Flask(__name__)
# app.config['DEBUG'] = Truefrom threading import Lock
from threading import Lock
from flask import Flask, render_template, session, request, jsonify, url_for
import time



app = Flask(__name__)

app.config['DEBUG'] = 'True'



@app.route('/')
def hello():
    return render_template('tabs.html')

@app.route('/read/<string:num>')
def readmyfile(num):
    fo = open("static/files/hodnoty.txt","r")
    rows = fo.readlines()
    return rows[int(num)-1]


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)