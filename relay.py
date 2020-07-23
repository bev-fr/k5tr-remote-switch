

from config import Config


class Data:
    state = {
        0: False,
        1: False,
        2: False,
        3: False,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
        9: False,
        10: False,
        11: False,
        12: False,
        13: False,
        14: False,
        15: False
    }

    bands = Config().bands()
    defaults = Config().defaults()
    mcp_board_list = Config().mcp_board_list()
    com_port = Config().com_port()
    relays = Config().relays()



class Relay:
    def setup():
        for relay in Data.state:
            if relay in Data.defaults:
                serialCtl.on(relay)
                Data.state[relay] = True
            else:
                serialCtl.off(relay)
                Data.state[relay] = False

    def bandOff(band):
        for relay in Data.bands[band]:
            serialCtl.off(relay)
            Data.state[relay] = False
    #Switches specified relay on
    def switchOn( band, index ):
        Relay.bandOff(band)
        serialCtl.on(index)
        Data.state[index] = True
        return None

    class Control:
        def write(addres, state):
            board = Data.mcp_board_list[addres[0]]
            mcp.Adafruit_MCP230XX(busnum = 1, address = board, num_gpios = 16)
            mcp.output(addres[0], state)
        def on(addres):
            self.write(addres, 1)

        def off(addres):
            self.write(addres, 0)

        def __init__(self):
            # Initialize the I2C bus and all pins
            for relay in Data.relays:
                board = Data.mcp_board_list[relay[0]]
                mcp = Adafruit_MCP230XX(busnum = 1, address = board, num_gpios = 16)
                mcp.config(relay[1], OUTPUT)

                # Create an instance of either the MCP23008 or MCP23017 class depending on
                # which chip you're using:
                # Use busnum = 0 for older Raspberry Pi's (256MB)
                # Use busnum = 1 for new Raspberry Pi's (512MB with mounting holes)
                # mcp = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)







Relay.setup()
