#!/usr/bin/python3
from flask import Flask, jsonify
import json
from flask import request


app = Flask(__name__)
users = {"jane": {
    "username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route('/')
def hello():
    return 'Welcome to the Flask API!'


@app.route('/data')
def data():
    usernames = []
    for user in users.values():
        usernames.append(user['username'])
    return jsonify(usernames)


@app.route('/status')
def status():
    return 'OK'


@app.route('/users/<username>')
def show_user(username):
    return jsonify(users[username])


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data['username']
    users[username] = {
            "username": username,
            "name": data['name'],
            "age": data['age'],
            "city": data['city']
    }
    return jsonify({
        "message": "User added",
        "user": users[username]
    })


if __name__ == "__main__":
    app.run()
