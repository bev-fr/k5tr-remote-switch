import sys
import serial

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
    com_port = Config().com_port()





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



class serialCtl:
    portName = Data.com_port

    def relayIndex(index):
        if (int(index) < 10):
            return str(index)
        else:
            return chr(55 + int(index))

    def write(index, state):
        serPort = serial.Serial(serialCtl.portName, 19200, timeout=1)
        serPort.write(str.encode("relay "+ str(state) + serialCtl.relayIndex(index) + "\n\r"))
        serPort.close()

    def on(index):
        serialCtl.write(index, "on ")

    def off(index):
        serialCtl.write(index, "off ")



Relay.setup()
