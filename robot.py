import RPi.GPIO as GPIO
import time

import motion.motors as controller
import sensors.ultrasonic as ultrasonic

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

motors = controller.Motors()
sensors = ultrasonic.Ultrasonic()

cmd = ""
while True:
    cmd = str(raw_input("Send command: "))
    print "Running: {0}".format(cmd)

    cmd_substr = cmd[0]

    if cmd_substr == "z":
        sensors.get_right_sensor()
        continue
    if cmd_substr == "x":
        sensors.get_left_sensor()
        continue
    if cmd_substr == "c":
        sensors.get_center_sensor()
        continue

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
        motors.set_left_pwm(float(cmd[1:]))
        continue
    if cmd_substr == "q":
        motors.set_right_pwm(float(cmd[1:]))
        continue
    if cmd_substr == "e":
        GPIO.cleanup()
        break

    time.sleep(1)
    pass
