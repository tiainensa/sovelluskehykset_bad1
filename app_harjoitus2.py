import mysql.connector
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/api/vehicles')
def get_all_vehicles_api():  # put application's code here
    with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
        with con.cursor(dictionary=True) as cur:
            cur.execute("SELECT * FROM vehicles")
            vehicles = cur.fetchall()
            return jsonify(vehicles)


@app.route('/vehicles')
def get_all_vehicles_page():  # put application's code here
    with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
        with con.cursor(dictionary=True) as cur:
            cur.execute("SELECT * FROM vehicles")
            vehicles = cur.fetchall()
            return render_template('vehicles/index.html', vehicles=vehicles)


if __name__ == '__main__':
    app.run()
