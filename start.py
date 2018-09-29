import sys
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

#init GPIO
channel_one = 20
channel_two = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_one, GPIO.OUT)
GPIO.setup(channel_two, GPIO.OUT)

def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off


# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor_args['2302'], 4)

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
count = 1

while count < 10:
    if __name__ == '__main__':
        try:
            if humidity is not None and temperature is not None:
                if temperature > 30 and temperature < 40:
                    motor_on(channel_two)
                else:
                    motor_off(channel_two)
    
                print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
            else:
                print('Failed to get reading. Try again!')
                sys.exit(1)

            time.sleep(1)
        except KeyboardInterrupt:
            GPIO.cleanup()
