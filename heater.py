import machine

heat_state = machine.Pin(3, machine.Pin.IN)
heat_out = machine.Pin(4, machine.Pin.OUT)
heat_trig = machine.Pin(5, machine.Pin.IN)
heat_time = 600*1000
def stop_heater(heat_o):
    heat_o.low()

def start_heater(heat_o):
    if(heat_out):
        tim.init(period=heat_time, mode=Timer.ONE_SHOT,
                callback=lambda t:stop_heater(heat_out))

tim = machine.Timer(4)
