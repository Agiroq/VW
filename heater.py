import machine
MIN = 10
heat_state = machine.Pin(3, machine.Pin.IN)
heat_out = machine.Pin(4, machine.Pin.OUT)
heat_trig = machine.Pin(14, machine.Pin.IN)
heat_time = 60000*MIN

def stop_heater(heat_o):
    heat_o.low()

def start_heater(heat_o, time):
    tim.init(period=time, mode=Timer.ONE_SHOT,
                callback=lambda t:stop_heater(heat_out))

tim = machine.Timer(4)

#trigger button define
heat_trig.irq(trigger=machine.Pin.IRQ_RISING,
              handler=lambda t:start_heater(heat_out, heat_time))
