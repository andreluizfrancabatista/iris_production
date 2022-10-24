from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask</h1>'