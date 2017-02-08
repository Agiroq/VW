import gas
GASANALOG = 0
ALARMLED = 13

gas = machine.ADC(GASANALOG)
gasLED = machine.Pin(ALARMLED, machine.Pin.OUT)

g = gas.CheckGas(led=gasLED, sensor=gas, time=1000)
