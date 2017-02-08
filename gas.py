import machine
from machine import Timer

GASANALOG = 0
ALARMLED = 13

gas = machine.ADC(GASANALOG)
gasLED = machine.Pin(ALARMLED, machine.Pin.OUT)

class checkGas():
    """docstring for checkGas."""
    def __init__(self, led=gasLED, sensor=gas, time=5000, level=480):
        super(checkGas, self).__init__()
        self.led = kargs['led']
        self.gas = kargs['sensor']
        self.timer = Timer(-1)
        self.level = level
        self.start()

    def checkGas():
        if (gas.read()>self.level):
            self.led.low()
            check = 1
        else:
            self.led.high()
            check = 0
        return check

    def start(time):
        self.timer.init(period=time, mode=Timer.PERIODIC,
                        callback=lambda t:checkGas())
    def stop():
        self.timer.deinit()
