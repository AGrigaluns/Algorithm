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


ufile = open('user.txt', 'r')
user = ufile.read()[:-1]
ufile.close()


pfile = open('password.txt', 'r')
password = pfile.read()[:-1]
pfile.close()

if __name__ == "__main__":
    app.run()


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


@app.route("/get_invoices/<int:id>/<string:year>/<string:month>", methods=['GET'])
def get_invoices(id, year, month):
    db = MySQLdb.connect("localhost", user, password, "musicshop")
    cur = db.cursor()
    proc = "get_invoices_by_empl"
    cur.callproc(proc, [id, year, month])

    columns = [x[0] for x in cur.description]
    data = cur.fetchall()
    json_data = []
    for result in data:
        json_data.append(dict(zip(columns, result)))
        print("json_data (proc):")
    print(json_data)
    response = {'data': json_data}
    return make_response(jsonify(json_data), 200)


@app.route("/create_artist/<string:artist_name>", methods=['POST'])
def create_artist(artist_name):
    db = MySQLdb.connect("localhost", user, password, "musicshop")
    cur = db.cursor()
    proc = "create_artist"
    cur.callproc(proc,[artist_name])
    response = {'data': f'["Name": "{artist_name}"]'}
    return make_response(jsonify(response), 200)


@app.route("/delete_artist/<int:id>", methods=['DELETE'])
def delete_artist(id):
    db = MySQLdb.connect("localhost", user, password, "musicshop")
    cur = db.cursor()
    proc = "delete_artist"
    results = cur.callproc(proc,[id])
    # cur.commit()
    print(results)
    response = {'data': f'["Deleted": "{id}"]'}
    return make_response(jsonify(response), 200)


@app.route("/update_artist/<int:id>/<string:new_artist_name>", methods=['PUT'])
def update_artist_by_id(id, new_artist_name):
    db = MySQLdb.connect("localhost", user, password, "musicshop")
    cur = db.cursor()
    proc = "update_artist"
    results = cur.callproc(proc,[id, new_artist_name])
    print(results)

    response = {'data': f'["Name": "{new_artist_name}"]'}
    return make_response(jsonify(response), 200)

