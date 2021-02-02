from flask import Flask, render_template, request, json, jsonify, current_app as app 
from datetime import date
import os
import requests

app = Flask(__name__)

@app.route('/')

@app.route('/nasa')
def nasa():
    today = str(date.today())
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=0hnWqUOzCWnNqLNddglJPGiG56sTs0PXg2hPY7MV&date='+today)

    data = response.json()

    return render_template('nasa.html', data=data)


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')