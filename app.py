from flask import Flask, render_template, redirect, url_for
import datetime

from relay import Data
from relay import Relay

app = Flask(__name__)

def button( band, index, label ):
    templateData = {
    'band': band,
    'index': index,
    'label': label
    }
    return render_template('button.html', **templateData, state = Data.state[index])

def bandItem( label ):
    templateData = {
    'band': label
    }
    return render_template('band.html', **templateData)


def button_list():
    resp = ""
    for band in Data.bands:
        resp = resp + bandItem(band)
        for relay in Data.bands[band]:
            resp = resp + (button(band, relay, Data.bands[band][relay]["label"]))
    return resp




@app.route('/alloff')
def forceRead():
    Relay.allOff()
    return redirect(url_for('home'))

@app.route('/<band>/<int:index>')
def index(band, index):
    Relay.switchOn(band, index)
    return redirect(url_for('home'))



@app.route("/")
def home():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    templateData = {
      'time': timeString,
      'button_list': button_list()
    }



    return render_template('index.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
