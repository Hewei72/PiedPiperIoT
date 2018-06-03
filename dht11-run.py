import RPi.GPIO as GPIO
import dht11
import time
import datetime
import tm1637

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# read data using pin 12
instance = dht11.DHT11(pin=12)

# initialize the display
display = tm1637.TM1637(clock_pin=5, data_pin=3)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        
        display_map = map(int,str(result.temperature)) + map(int,str(result.humidity))
        display.set_values(display_map)

    time.sleep(1)
