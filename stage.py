# from flask import Flask, redirect, url_for, request
# app = Flask(__name__)
#
#
#
#
#
# @app.route("/")
# def home():
#     now = datetime.datetime.now()
#     timeString = now.strftime("%Y-%m-%d %H:%M:%S")
#     templateData = {
#       'time': timeString,
#       'button_list': button_list()
#     }
#     return render_template('index.html', **templateData)
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80, debug=True)
#
#
#
#
#
#
# @app.route('/',methods = ['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['nm']
#         return redirect(url_for('success',name = user))
#     else:
#         user = request.args.get('nm')
#         return redirect(url_for('success',name = user))
#
#     return render_template('index.html', **templateData)
# if __name__ == '__main__':
#    app.run(debug = True)


import yaml



class Config:
    cfg = None
    def __init__(self):
        with open("config.yml", "r") as ymlfile:
            self.cfg = yaml.load(ymlfile)
        # return cfg["data"]["bands"]

    def bands(self):
        return self.cfg["config"]["bands"]

    def defaults(self):
        return self.cfg["config"]["default_on"]

    def mcp_board_list(self):
        return self.cfg["config"]["mcp_board_list"]

    def relays(self):
        relays = []
        for band in self.cfg["config"]["bands"]:
            for relay in self.cfg["config"]["bands"][band]:
                relays.append(relay["address"])
        return relays

relays = Config().relays()

print(relays)
# appData = Data()
#
# print(appData.bands())
#
# for band in appData.bands():
#     print(band)
#     for relay in appData.bands()[band]:
#         print(relay)
