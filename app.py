from flask import Flask, render_template, redirect, url_for
import datetime

from relay import Data
from relay import Relay

app = Flask(__name__)
relayCtl = Relay()
data = Data(relayCtl)

def button( band, relay ):
    address = tuple(relay["address"])
    label = relay["label"]
    templateData = {
    'band': band,
    'index': 'x'.join(str(address) for address in address),
    'label': label
    }
    return render_template('button.html', **templateData, state = Data.state[address])


def bandItem( label ):
    templateData = {'band': label}
    return render_template('band.html', **templateData)


def button_list(data):
    button_list = ""
    for band in data.bands:
        button_list = button_list + bandItem(band)
        for relay in data.bands[band]:
            button_list = button_list + (button(band, relay))
    return button_list


@app.route('/<band>/<index>')
def index(band, index):
    address = tuple(map(int, index.split('x')))
    relayCtl.switchOn(band, address)
    return redirect(url_for('home'))



@app.route("/")
def home():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    templateData = {
      'time': timeString,
      'button_list': button_list(data)
    }
    return render_template('index.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
