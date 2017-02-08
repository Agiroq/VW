import machine, time
from machine import Timer

GASANALOG = 0
ALARMLED = 13

gasA = machine.ADC(GASANALOG)
gasLED = machine.Pin(ALARMLED, machine.Pin.OUT)
class CheckGas():
    """docstring for checkGas."""
    def __init__(self, led, sensor, time=5000, level=480):
        super(CheckGas, self).__init__()
        self.led = led
        self.led.high()
        time.sleep_ms(500)
        self.led.low()
        time.sleep_ms(500)
        self.led.high()
        time.sleep_ms(500)
        self.led.low()
        self.gas = sensor
        self.timer = Timer(-1)
        self.level = level
        self.time = time
        self.start(self.time)

    def checkGas(self):
        value = self.gas.read()
        check = 0
        if (self.gas.read()>self.level):
            self.led.high()
            check = 1

        else:
            self.led.low()
            check = 0

        print(value, check)
        return check

    def start(self, time):
        self.timer.init(period=time, mode=Timer.PERIODIC,
                        callback=lambda t:self.checkGas())
    def stop(self):
        self.timer.deinit()


g = CheckGas(gasLED, gasA, 5000)
