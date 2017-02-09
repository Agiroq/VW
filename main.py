import machine
from machine import Timer

GASANALOG = 0
ALARMLED = 13
TIMECHECK = 5000
LLINDAR_GAS = 480

gasA = machine.ADC(GASANALOG)
gasLED = machine.Pin(ALARMLED, machine.Pin.OUT)

def checkGas(sensor, level):
    value = sensor.read()
    check = 0
    if (value>level):
        self.led.high()
        check = 1
    print(value, check)
    return check

def gasCheck_start(timer, time, sensor, level):
    timer.init(period=time, mode=Timer.PERIODIC,
                    callback=lambda t:self.checkGas(sensor, level))
def gasCheck_stop(timer):
    timer.deinit()

t = machine.Timer(-1)
gasCheck_start(t, TIMECHECK, gasA, LLINDAR_GAS)
