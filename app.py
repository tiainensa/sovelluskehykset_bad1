import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/users')
def get_all_users():  # put application's code here
    with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
        with con.cursor() as cur:
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()
            return jsonify(users)


if __name__ == '__main__':
    app.run()
