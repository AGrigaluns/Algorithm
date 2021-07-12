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


@app.route("/create_artist/<int:id>/<string:name>", methods=['POST'])
def create_artist(id, name):
    db = MySQLdb.connect("localhost", user, password, "musicshop")
    cur = db.cursor()
    query = "INSERT INTO artists VALUES ArtistId=" + str(id), "Name=" + str(name)
    cur.execute(query)
    json_data = cur.fetchall()
    cur.close()
    print("json_data (creare_artist):")
    print(json_data)
    return jsonify(data=json_data)


@app.route("/delete_types/<int:id>", methods=['DELETE'])
def delete_types(id):
    db = MySQLdb.connect("localhost", user, password, "musicshop")
    cur = db.cursor()
    query = "DELETE FROM media_types WHERE MediaTypeId=" + str(id)
    cur.execute(query)
    json_data = cur.fetchall()
    cur.close()
    print("json_data (delete_types):")
    print(json_data)
    return jsonify(data=json_data)


@app.route("/add_types/<int:id>/<string:name>", methods=['PUT'])
def update_genres(id, name):
    db = MySQLdb.connect("localhost", user, password, "musicshop")
    cur = db.cursor()
    query = "UPDATE genres SET Name=" + str(name), "WHERE GenreId=" + str(id)
    cur.execute(query)
    json_data = cur.fetchall()
    cur.close()
    print("json_data (update_genres):")
    print(json_data)
    return jsonify(data=json_data)

