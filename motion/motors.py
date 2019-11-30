import RPi.GPIO as GPIO
import time

class Motors:

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

    def __init__(self):

        GPIO.setup(self.MOTOR_LEFT_1, GPIO.OUT)
        GPIO.output(self.MOTOR_LEFT_1, GPIO.LOW)

        GPIO.setup(self.MOTOR_LEFT_2, GPIO.OUT)
        GPIO.output(self.MOTOR_LEFT_2, GPIO.LOW)

        GPIO.setup(self.MOTOR_RIGHT_1, GPIO.OUT)
        GPIO.output(self.MOTOR_RIGHT_1, GPIO.LOW)

        GPIO.setup(self.MOTOR_RIGHT_2, GPIO.OUT)
        GPIO.output(self.MOTOR_RIGHT_2, GPIO.LOW)

        GPIO.setup(self.MOTOR_LEFT_ENABLE, GPIO.OUT)
        GPIO.setup(self.MOTOR_RIGHT_ENABLE, GPIO.OUT)

        self.leftMotor = GPIO.PWM(self.MOTOR_LEFT_ENABLE, 1000)
        self.rightMotor = GPIO.PWM(self.MOTOR_RIGHT_ENABLE, 1000)

        self.leftMotor.start(self.MOTOR_LEFT_PWM)
        self.rightMotor.start(self.MOTOR_RIGHT_PWM)

        pass


    def go_backward(self):
        GPIO.output(self.MOTOR_LEFT_1, GPIO.HIGH)
        GPIO.output(self.MOTOR_LEFT_2, GPIO.LOW)

        GPIO.output(self.MOTOR_RIGHT_1, GPIO.HIGH)
        GPIO.output(self.MOTOR_RIGHT_2, GPIO.LOW)
        time.sleep(1)
        pass

    def go_forward(self):
        GPIO.output(self.MOTOR_LEFT_1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_2, GPIO.HIGH)

        GPIO.output(self.MOTOR_RIGHT_1, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_2, GPIO.HIGH)
        time.sleep(1)
        pass

    def turn_left(self):
        GPIO.output(self.MOTOR_LEFT_1, GPIO.HIGH)
        GPIO.output(self.MOTOR_LEFT_2, GPIO.LOW)

        GPIO.output(self.MOTOR_RIGHT_1, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_2, GPIO.HIGH)
        time.sleep(1)
        pass

    def turn_right(self):
        GPIO.output(self.MOTOR_LEFT_1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_2, GPIO.HIGH)

        GPIO.output(self.MOTOR_RIGHT_1, GPIO.HIGH)
        GPIO.output(self.MOTOR_RIGHT_2, GPIO.LOW)
        time.sleep(1)
        pass

    def set_left_pwm(self, value):
        self.MOTOR_LEFT_PWM = value
        self.leftMotor.ChangeDutyCycle(value)
        pass

    def set_right_pwm(self, value):
        self.MOTOR_RIGHT_PWM = value
        self.rightMotor.ChangeDutyCycle(value)
        pass


