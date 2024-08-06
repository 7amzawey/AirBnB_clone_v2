#!/usr/bin/python3
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """display a HTML page that shows a list of the states"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-state_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """close the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
