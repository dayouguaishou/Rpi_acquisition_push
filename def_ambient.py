from apds9960.const import *
from apds9960 import APDS9960
import RPi.GPIO as GPIO
import smbus
from time import sleep

port = 1
bus = smbus.SMBus(port)

apds = APDS9960(bus)

def intH(channel):
    print("INTERRUPT")

def read_ambient(io = 7):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(io, GPIO.IN)
    try:
        # Interrupt-Event hinzufuegen, steigende Flanke
        GPIO.add_event_detect(io, GPIO.FALLING, callback = intH)
        #print("Light Sensor Test")
        #print("=================")
        apds.enableLightSensor()
        oval = -1
        sleep(0.25)
        val = 0
        val = apds.readAmbientLight()
        if val != oval:
            #print("AmbientLight={}".format(val))
            oval = val
        GPIO.cleanup()

    except:
        GPIO.cleanup()
        val = -1
        print "error in read_ambient"

    return  val


#print (read_ambient())
