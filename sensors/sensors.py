import RPi.GPIO as GPIO
import time

# Ultrasonic Sensors
SENSOR_0_TRIGGER = 23
SENSOR_0_ECHO = 24

SENSOR_1_TRIGGER = 18
SENSOR_1_ECHO = 17

SENSOR_2_TRIGGER = 22
SENSOR_2_ECHO = 27

def setup_sensors():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    # Setup Sensor 0
    GPIO.setup(SENSOR_0_TRIGGER, GPIO.OUT)
    GPIO.output(SENSOR_0_TRIGGER, GPIO.LOW)

    GPIO.setup(SENSOR_0_ECHO, GPIO.IN)

    # Setup Sensor 1
    GPIO.setup(SENSOR_1_TRIGGER, GPIO.OUT)
    GPIO.output(SENSOR_1_TRIGGER, GPIO.LOW)

    GPIO.setup(SENSOR_1_ECHO, GPIO.IN)

    # Setup Sensor 2
    GPIO.setup(SENSOR_2_TRIGGER, GPIO.OUT)
    GPIO.output(SENSOR_2_TRIGGER, GPIO.LOW)

    GPIO.setup(SENSOR_2_ECHO, GPIO.IN)

    pass



def get_distance(trigger, echo):
    """
    Returns the sensor distance
    """
    GPIO.output(trigger, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger, GPIO.LOW)

    while GPIO.input(echo) == 0:
        #print "PIN {0} == 0".format(echo)
        pass
    start = time.time()

    while GPIO.input(echo) == 1:
        #print "PIN {0} == 1".format(echo)
        pass
    stop = time.time()

    return (stop - start) * 17000


# print "Starting Measurement SENSOR[0]..."
# print get_distance(SENSOR_0_TRIGGER, SENSOR_0_ECHO)

# print "Starting Measurement SENSOR[1]..."
# print get_distance(SENSOR_1_TRIGGER, SENSOR_1_ECHO)

# print "Starting Measurement SENSOR[2]..."
# print get_distance(SENSOR_2_TRIGGER, SENSOR_2_ECHO)

# GPIO.cleanup()
