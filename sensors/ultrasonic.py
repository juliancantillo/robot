import RPi.GPIO as GPIO
import time

class Ultrasonic:

    # Ultrasonic Sensors
    SENSOR_0_TRIGGER = 23
    SENSOR_0_ECHO = 24

    SENSOR_1_TRIGGER = 18
    SENSOR_1_ECHO = 17

    SENSOR_2_TRIGGER = 22
    SENSOR_2_ECHO = 27

    def __init__(self):
        # Setup Sensor 0
        GPIO.setup(self.SENSOR_0_TRIGGER, GPIO.OUT)
        GPIO.output(self.SENSOR_0_TRIGGER, GPIO.LOW)

        GPIO.setup(self.SENSOR_0_ECHO, GPIO.IN)

        # Setup Sensor 1
        GPIO.setup(self.SENSOR_1_TRIGGER, GPIO.OUT)
        GPIO.output(self.SENSOR_1_TRIGGER, GPIO.LOW)

        GPIO.setup(self.SENSOR_1_ECHO, GPIO.IN)

        # Setup Sensor 2
        GPIO.setup(self.SENSOR_2_TRIGGER, GPIO.OUT)
        GPIO.output(self.SENSOR_2_TRIGGER, GPIO.LOW)

        GPIO.setup(self.SENSOR_2_ECHO, GPIO.IN)

        pass

    def get_right_sensor(self):
        return get_distance(trigger=self.SENSOR_0_TRIGGER, echo=self.SENSOR_0_ECHO)

    def get_left_sensor(self):
        return get_distance(trigger=self.SENSOR_2_TRIGGER, echo=self.SENSOR_2_ECHO)

    def get_center_sensor(self):
        return get_distance(trigger=self.SENSOR_1_TRIGGER, echo=self.SENSOR_1_ECHO)

    def get_distance(trigger, echo):
        """
        Returns the sensor distance
        """
        GPIO.output(trigger, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trigger, GPIO.LOW)

        while GPIO.input(echo) == 0:
            pass
        start = time.time()

        while GPIO.input(echo) == 1:
            pass
        stop = time.time()

        return (stop - start) * 17000


    # print "Starting Measurement SENSOR[0]..."
    # print get_distance(self.SENSOR_0_TRIGGER, self.SENSOR_0_ECHO)

    # print "Starting Measurement SENSOR[1]..."
    # print get_distance(self.SENSOR_1_TRIGGER, self.SENSOR_1_ECHO)

    # print "Starting Measurement SENSOR[2]..."
    # print get_distance(self.SENSOR_2_TRIGGER, self.SENSOR_2_ECHO)

    # GPIO.cleanup()
