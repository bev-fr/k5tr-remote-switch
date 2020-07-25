from config import Config
#https://learn.adafruit.com/mcp230xx-gpio-expander-on-the-raspberry-pi/using-the-library

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
    def on(self, address):
        print("on")
        print(address)

    def off(self, address):
        print("off")
        print(address)

    def __init__(self):
        print("init")
    # class Control:
    #     mcpArray = []
    #     def write(address, state):
    #         board = Data.mcp_board_list[address[0]]
    #         board.output(address[0], state)
    #
    #     def on(address):
    #         self.write(address, 1)
    #
    #     def off(address):
    #         self.write(address, 0)
    #
    #     def __init__(self):
    #         # Initialize the I2C bus and all pins
    #         for board in Data.mcp_board_list:
    #             self.mcpArray.append( Adafruit_MCP230XX(busnum = 1, address = board, num_gpios = 16))
    #         for address in Data.relays:
    #             self.mcpArray[address[0]].config(address[2], OUTPUT)
    #             # Create an instance of either the MCP23008 or MCP23017 class depending on
    #             # which chip you're using:
    #             # Use busnum = 0 for older Raspberry Pi's (256MB)
    #             # Use busnum = 1 for new Raspberry Pi's (512MB with mounting holes)
    #             # mcp = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)
