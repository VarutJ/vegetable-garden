import sys
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

#init GPIO
#Relay
channel_one = 21
channel_two = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Relay
GPIO.setup(channel_one, GPIO.OUT)
GPIO.setup(channel_two, GPIO.OUT)

GPIO.output(channel_one, GPIO.HIGH)
GPIO.output(channel_two, GPIO.HIGH)

#Light Relay
GPIO.setup(19, GPIO.OUT) # GREEN
GPIO.setup(26, GPIO.OUT) # RED

#Motion
motion_pin = 12
GPIO.setup(motion_pin, GPIO.IN)

#Water
water_pin = 16
GPIO.setup(water_pin, GPIO.IN)

def water_not_found(relay_pin):
    print "Open water"
    GPIO.output(relay_pin, GPIO.LOW)  # Turn motor on

def water_detech(relay_pin):
    print "Close water"
    GPIO.output(relay_pin, GPIO.HIGH)  # Turn motor off

def MOTION(motion_pin):
    print "Motion Detected!"

def motor_on(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor on

def motor_off(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor off

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).

#humidity, temperature = Adafruit_DHT.read_retry(sensor_args['2302'], 4)

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

#motor_off(channel_one)
#motor_off(channel_two)
count = 1

while count < 10:
    if __name__ == '__main__':
        try:
            humidity, temperature = Adafruit_DHT.read_retry(sensor_args['2302'], 4)
            
            if humidity is not None and temperature is not None:
                if temperature > 31:
                    print("working")
                    motor_on(channel_two)
                    GPIO.output(26,GPIO.HIGH)
                    GPIO.output(19,GPIO.LOW)
                else:
                    print("Not working")
                    motor_off(channel_two)
                    GPIO.output(26,GPIO.LOW)
                    GPIO.output(19,GPIO.HIGH)

                if GPIO.input(motion_pin):
                    MOTION(motion_pin)
                else:
                    print("None")

                if GPIO.input(water_pin):
                    water_detech(channel_one)
                else:
                    water_not_found(channel_one)

                print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
            else:
                print('Failed to get reading. Try again!')
                sys.exit(1)

            time.sleep(1)
        except KeyboardInterrupt:
            GPIO.cleanup()