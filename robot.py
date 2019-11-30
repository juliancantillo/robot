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
        print "Right sensor {}".format(sensors.get_right_sensor())
        continue
    if cmd_substr == "x":
        print "Left sensor {}".format(sensors.get_left_sensor())
        continue
    if cmd_substr == "c":
        print "Middle sensor {}".format(sensors.get_center_sensor())
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

def calculate_pwm(value):
    return (value * 5) + 50

while True:

    right_distance = sensors.get_right_sensor()
    left_distance = sensors.get_left_sensor()
    center_distance = sensors.get_center_sensor()

    if center_distance < 3.0:

        if right_distance < left_distance:
            motors.turn_left()
            continue

        motors.turn_right()
        continue

    if right_distance < 10.0:
        motors.set_right_pwm(calculate_pwm(right_distance))
        continue

    if left_distance < 10.0:
        motors.set_left_pwm(calculate_pwm(left_distance))
        continue

    if right_distance >= 10.0:
        motors.set_right_pwm(100)
        continue

    if left_distance >= 10.0:
        motors.set_left_pwm(100)
        continue

    motors.go_backward()
