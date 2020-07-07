import yaml



class Config:
    cfg = None
    def __init__(self):
        with open("config.yml", "r") as ymlfile:
            self.cfg = yaml.load(ymlfile)
        # return cfg["data"]["bands"]

    def bands(self):
        return self.cfg["data"]["bands"]


# appData = Data()
#
# print(appData.bands())
#
# for band in appData.bands():
#     print(band)
#     for relay in appData.bands()[band]:
#         print(relay)
