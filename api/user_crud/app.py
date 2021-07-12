from flask import Flask, send_from_directory, jsonify, make_response
from flask_cors import CORS

import MySQLdb
import os
import json

app = Flask(__name__, static_url_path='/')
cors = CORS(app)


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('./', path)


if __name__ == "__main__":
    app.run()


ufile = open('user.txt', 'r')
user = ufile.read()[:-1]
ufile.close()


pfile = open('password.txt', 'r')
password = pfile.read()[:-1]
pfile.close()


@app.route("/select")
def select():
    db = MySQLdb.connect("localhost", user, password, "musicshop")
    cur = db.cursor()
    query = "SELECT * FROM artists WHERE ArtistId=1"
    cur.execute(query)
    json_data = cur.fetchall()
    print("json_data (select):")
    print(json_data)
    return jsonify(data=json_data)


@app.route("/select/<int:id>")
def select_by_id(id):
    db = MySQLdb.connect("localhost", user, password, "musicshop")
    cur = db.cursor()
    query = "SELECT * FROM artists WHERE ArtistId=" + str(id)
    #query = "SELECT * FROM artists WHERE ArtistId=%s" % (id)
    cur.execute(query)
    json_data = cur.fetchall()
    cur.close()
    print("json_data (select):")
    print(json_data)
    return jsonify(data=json_data)
