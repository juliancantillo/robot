import RPi.GPIO as GPIO
import time

import motion.motors as controller

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

motors = controller.Motors()

cmd = ""
while True:
    cmd = str(raw_input("Send command: "))
    print "Running: {0}".format(cmd)

    cmd_substr = cmd[0]

    if cmd_substr == "l":
        motors.turn_left()
        continue
    if cmd_substr == "r":
        motors.turn_right()
        continue
    if cmd_substr == "f":
        motors.go_forward()
        continue
    if cmd_substr == "b":
        motors.go_backward()
        continue
    if cmd_substr == "p":
        motors.MOTOR_LEFT_PWM = float(cmd[1:])
        motors.leftMotor.ChangeDutyCycle(MOTOR_LEFT_PWM)
        continue
    if cmd_substr == "q":
        motors.MOTOR_RIGHT_PWM = float(cmd[1:])
        motors.rightMotor.ChangeDutyCycle(MOTOR_RIGHT_PWM)
        continue
    if cmd_substr == "e":
        GPIO.cleanup()
        break

    time.sleep(1)
    pass
