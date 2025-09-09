from machine import Pin, PWM
from time import sleep

#instead of import machine ->
# we make machine now jus Pin


#SETUP
mode = "On" 
dimmer = PWM(Pin(15))
dimmer.freq(1000)

#led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin. PULL_DOWN)
    
def toggle_led(pin):
    global mode
    if(mode == "On"):
       mode = "Fade"
    elif(mode == "Fade"): # else if in python
        mode = "On"
    
    #dimmer.duty_u16(65535)
    #print(f"button status level: {dimmer.duty_u16()}")
    #print(led.value())
    
button.irq(trigger=Pin.IRQ_FALLING, handler=toggle_led)    
    
#LOOP

while True:
    if (mode == "On"):
        dimmer.duty_u16(65535) #has light at max brightness
        sleep(1)               #nighty night
    elif(mode == "Fade"):
        for duty in range(65535):
            dimmer.duty_u16(duty)
            sleep(0.0001)

        for duty in range(65535, 2, -1):
            dimmer.duty_u16(duty)
            sleep(0.0001)

