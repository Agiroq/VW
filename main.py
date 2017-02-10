import machine
from machine import Timer

#constants
MIN_HEAT = 10
TIMECHECK = 5000
LLINDAR_GAS = 480

#pins     CODE  BOARD
GASANALOG = 0   #A0
GASALARM = 13   #D7
HEAT_O = 14     #D5
HEAT_T = 12     #D6
HEAT_I = 4      #D2

gasA = machine.ADC(GASANALOG)
gasLED = machine.Pin(GASALARM, machine.Pin.OUT)

heat_state = machine.Pin(HEAT_I, machine.Pin.IN)
heat_out = machine.Pin(HEAT_O, machine.Pin.OUT)
heat_trig = machine.Pin(HEAT_T, machine.Pin.IN)
heat_time = 60000*MIN_HEAT

#function definitions

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

def stop_heater(heat_o):
    heat_o.low()

def start_heater(timer, heat_o, time):
    timer.init(period=time, mode=Timer.ONE_SHOT,
                callback=lambda t:stop_heater(heat_out))

tim = machine.Timer(4)

#trigger button define
heat_trig.irq(trigger=machine.Pin.IRQ_RISING,
              handler=lambda t:start_heater(tim, heat_out, heat_time))

t = machine.Timer(-1)
gasCheck_start(tim, TIMECHECK, gasA, LLINDAR_GAS)
