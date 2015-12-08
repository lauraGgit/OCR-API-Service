import os
import logging
from logging import Formatter, FileHandler
from flask import Flask, request, abort, jsonify, make_response

from ocr import image_string

app = Flask(__name__)
_VERSION = 1 # API Version

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/ocr/api/v{}/almonds'.format(_VERSION), methods=['GET'])
def ocr_almond():
    almonds = image_string('https://butterflyofdream.files.wordpress.com/2013/05/ocr-sample2.png')
    return jsonify({'output': almonds})

@app.route('/ocr/api/v{}/'.format(_VERSION), methods=['POST'])
def ocr():
    if not request.json or not 'image_url' in request.json:
        abort(400)
    text = image_string(request.json['image_url'])
    return jsonify({'output': text})

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(debug=True)
