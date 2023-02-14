#from flask_restful import Api, Resource, reqparse
from summary import summarize
from flask import Flask, request

app = Flask(__name__)

# Define your Flask API endpoint
@app.route('/api/summarize', methods=['POST'])
def summarize():
    input_string = request.json.get('input_string')
    summary = summarize(input_string,1.5)
    return summary

if __name__ == '__main__':
    app.run()
