import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

""" Mikä tässä koodissa on vikana?

Jos tätä arvoidaan vain sillä perusteella, toimiiko kaikki, niin koodissa ei ole mitään vikaa, koska kaikki ominaisuudet
toimivat oikein

Arkkitehtuurin näkökulmasta koodi on aivan käyttökelvotonta.

Tehdään tämä seuraavaksi käyttäen MVC:tä.

"""


@app.route('/api/products')
def get_all_products():
    with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
        with con.cursor(dictionary=True) as cur:
            cur.execute("SELECT * FROM products")
            products = cur.fetchall()
            return jsonify(products)


@app.route('/api/users')
def get_all_users():  # put application's code here
    with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
        with con.cursor(dictionary=True) as cur:
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()
            return jsonify(users)


if __name__ == '__main__':
    app.run()
