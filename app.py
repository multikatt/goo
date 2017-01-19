from flask import Flask, g
import sqlite3
import os

app = Flask(__name__)

app.config.update(
    DB_PATH=os.getcwd()+"/db.sql"
)


def create_db():
    db_path = app.config["DB_PATH"]
    g.db = sqlite3.connect(db_path)
    g.db.commit()


@app.teardown_appcontext
def close_db(error):
    db_path = app.config["DB_PATH"]
    if hasattr(g, "db"):
        g.db.close()
        os.unlink(db_path)


@app.route("/")
def hello():
    return "hello"


if __name__ == "__main__":
    app.run()
