from flask import Flask
from flask.json import jsonify
from flask import request
import pandas as pd
import os
import socket
import pickle
import ujson

app = Flask(__name__)


count_vect = pickle.load(open('pkls/model.pkl', 'rb'))
tf_transformer = pickle.load(open('pkls/model.pkl', 'rb'))
model = pickle.load(open('pkls/model.pkl', 'rb'))

@app.route("/", methods=["POST"])
def main():
    if request.json:
        text = ujson.loads(text)
        if isinstance(text, dict):
            if 'text_review' in text.keys():
                text = text['text_review']
                text = request.json.lower().replace('[\.,&;\(\)]', '')
                counts = count_vect.transform(pd.Series(text))
                transformed = tf_transformer.transform(counts)
                sentiment = 'Positive' if model.predict(transformed) else 'Negative'
                return jsonify({'sentiment', sentiment}), 200
    return '', 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=805)