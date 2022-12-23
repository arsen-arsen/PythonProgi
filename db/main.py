from flask import Flask, jsonify, request, redirect, url_for, render_template
import psycopg2
import random
from config import config

app = Flask(__name__)

try:
    params = config()
    print('Connecting to database...')
    connection = psycopg2.connect(**params)
    connection.autocommit = True
    cursor = connection.cursor()
    print('PostgreSQL DB version: ')
    cursor.execute('SELECT version()')
    db_version = cursor.fetchone()
    print(db_version)
except(Exception, psycopg2.DatabaseError) as error:
    print(error)

data = []


@app.route("/home")
def homepage():
    return render_template("index.html")


@app.route('/users', methods=['GET'])
def users_get():
    sql = 'SELECT * FROM users;'
    cursor.execute(sql)
    data = cursor.fetchall()
    return render_template("users.html", data = data)


@app.route('/users/<userid>', methods=['GET'])
def userid_get():
    sql = 'SELECT * FROM users WHERE id = %s'
    cursor.execute(sql, (str(),) )
    data = cursor.fetchall()
    print(data)
    return data


@app.route('/users', methods=['POST'])
def user_add():
    sql = 'INSERT INTO users VALUES (%s, %s ,%s)'
    id = random.randint(0, 100000)
    name = request.json['name']
    surname = request.json['surname']
    proglang = request.json['prog_lang']
    cursor.execute(sql, (id, name, surname, proglang))
    connection.commit()
    return userid_get(id), data


@app.route('/users', methods=['DELETE'])
def user_del():
    data.pop(request.get_json()['id'])
    return data


@app.route('/users', methods=['PUT'])
def user_upd():
    updsql = """ UPDATE users
                    SET first_name = %s
                    SET last_name = %s
                    SET prog_lang = %s
                    WHERE id = %s"""
    id = request.json['id']
    name = request.json['first_name']
    surname = request.json['last_name']
    proglang = request.json['prog_lang']
    cursor.execute(updsql, (id, name, surname, proglang))
    return data

if __name__ == '__main__':
    app.run(debug=True)
