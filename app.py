import flask
import json
import os
from flask import send_from_directory, request
import requests as r


# Flask app should start in global layout
app = flask.Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')


@app.route('/')
@app.route('/home')
def home():
    return 'ok'


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    print(req)
    url = r.get(
        'https://raw.githubusercontent.com/muhiqsimui/PyTraining/fun/dataLine.json')
    data = url.json()

    balasan = str(data['pesan'])

    query_result = req.get('queryResult')
    output = str(query_result['queryText'][5:])

    return {
        'fulfillmentText': 'Selamat hari raya idul adha tahun '+output+' Hijriah'
    }


if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()
