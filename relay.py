from config import Config
import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017


class Data:
    config = Config()
    state = {
        (0,1): False
    }

    bands = config.bands()
    defaults = config.defaults()
    mcp_board_list = config.mcp_board_list()
    relays = config.relays()

    def __init__(self, relayCtl):
        for address in self.relays:
            address = tuple(address)
            if address in self.defaults:
                relayCtl.control.on(address)
                self.state[address] = True
            else:
                self.state[address] = False



class Relay:
    def bandOff(self, band):
        for relay in Data.bands[band]:
            address = tuple(relay["address"])
            self.control.off(address)
            Data.state[address] = False

    #Switches specified relay on
    def switchOn(self, band, address):
        self.bandOff(band)
        self.control.on(address)
        Data.state[address] = True
        return None
    def __init__(self):
        self.control = Control()



class Control:
    mcpArray = []
    pins = {}
    def write(self, address, state):
        self.pins[address].value = state


    def on(self, address):
        self.write(address, False)

    def off(self, address):
        self.write(address, True)

    def __init__(self):

        i2c = busio.I2C(board.SCL, board.SDA)
        # Initialize the I2C bus and all pins
        for i2cAddr in Data.mcp_board_list:
            mcp = MCP23017(i2c, address=i2cAddr)
            self.mcpArray.append(mcp)

        for address in Data.relays:
            self.pins[address] = self.mcpArray[address[0]].get_pin(address[1])
            self.pins[address].switch_to_output(value=True)
