import yaml
import re



class Config:
    cfg = None
    def __init__(self):

        #load the config
        with open("config.yml", "r") as ymlfile:
            self.cfg = yaml.safe_load(ymlfile)

    # an array of bands, each band has an array of antennas
    def bands(self):
        return self.cfg["config"]["bands"]

    # an array of relays that default on
    def defaults(self):
        defaults = []
        for address in self.cfg["config"]["default_on"]:
            defaults.append(tuple(address))
        return defaults

    # an array of MCP addresses
    def mcp_board_list(self):
        return self.cfg["config"]["mcp_board_list"]

    # an array of relays
    def relays(self):
        relays = []
        for band in self.cfg["config"]["bands"]:
            for relay in self.cfg["config"]["bands"][band]:
                relays.append((tuple(relay["address"])))
        return relays
