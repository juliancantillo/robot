import RPi.GPIO as GPIO
import time

# Motors
MOTOR_LEFT_1 = 5
MOTOR_LEFT_2 = 6

MOTOR_RIGHT_1 = 16
MOTOR_RIGHT_2 = 26

MOTOR_LEFT_ENABLE = 12
MOTOR_RIGHT_ENABLE = 13

MOTOR_LEFT_PWM = 70
MOTOR_RIGHT_PWM = 70

leftMotor =  None
rightMotor = None

def setup_motors():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    GPIO.setup(MOTOR_LEFT_1, GPIO.OUT)
    GPIO.output(MOTOR_LEFT_1, GPIO.LOW)

    GPIO.setup(MOTOR_LEFT_2, GPIO.OUT)
    GPIO.output(MOTOR_LEFT_2, GPIO.LOW)

    GPIO.setup(MOTOR_RIGHT_1, GPIO.OUT)
    GPIO.output(MOTOR_RIGHT_1, GPIO.LOW)

    GPIO.setup(MOTOR_RIGHT_2, GPIO.OUT)
    GPIO.output(MOTOR_RIGHT_2, GPIO.LOW)

    GPIO.setup(MOTOR_LEFT_ENABLE, GPIO.OUT)
    GPIO.setup(MOTOR_RIGHT_ENABLE, GPIO.OUT)

    leftMotor = GPIO.PWM(MOTOR_LEFT_ENABLE, 1000)
    rightMotor = GPIO.PWM(MOTOR_RIGHT_ENABLE, 1000)

    leftMotor.start(MOTOR_LEFT_PWM)
    rightMotor.start(MOTOR_RIGHT_PWM)

    pass


def go_backward():
    GPIO.output(MOTOR_LEFT_1, GPIO.HIGH)
    GPIO.output(MOTOR_LEFT_2, GPIO.LOW)

    GPIO.output(MOTOR_RIGHT_1, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT_2, GPIO.LOW)
    time.sleep(1)
    pass

def go_forward():
    GPIO.output(MOTOR_LEFT_1, GPIO.LOW)
    GPIO.output(MOTOR_LEFT_2, GPIO.HIGH)

    GPIO.output(MOTOR_RIGHT_1, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_2, GPIO.HIGH)
    time.sleep(1)
    pass

def turn_left():
    GPIO.output(MOTOR_LEFT_1, GPIO.HIGH)
    GPIO.output(MOTOR_LEFT_2, GPIO.LOW)

    GPIO.output(MOTOR_RIGHT_1, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_2, GPIO.HIGH)
    time.sleep(1)
    pass

def turn_right():
    GPIO.output(MOTOR_LEFT_1, GPIO.LOW)
    GPIO.output(MOTOR_LEFT_2, GPIO.HIGH)

    GPIO.output(MOTOR_RIGHT_1, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT_2, GPIO.LOW)
    time.sleep(1)
    pass
