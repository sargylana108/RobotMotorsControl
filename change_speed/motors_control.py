# Imports 
import RPi.GPIO as GPIO
import time
import sys

# Configuring GPIO pin numbers for motor control
motor_pins = {'left': (17, 18), 'right': (22, 23)}
pwm_objects = {}

# GPIO and PWM initialisation
def init():
    GPIO.setmode(GPIO.BCM)
    for key, pin_pair in motor_pins.items():
        GPIO.setup(pin_pair, GPIO.OUT)
        pwm_objects[key] = (GPIO.PWM(pin_pair[0], 100), GPIO.PWM(pin_pair[1], 100))
        pwm_objects[key][0].start(0)
        pwm_objects[key][1].start(0)

# Stopping all motors anf PWM
def stop():
    for pwm_pair in pwm_objects.values():
        pwm_pair[0].ChangeDutyCycle(0)
        pwm_pair[1].ChangeDutyCycle(0)

# Speed change
def change_speed(pin, start_duty, end_duty, step=1):
    if start_duty < end_duty:  # Speedup
        for duty in range(start_duty, end_duty + 1, step):
            pin.ChangeDutyCycle(duty)
            time.sleep(0.1)
    else:  # Slowdown
        for duty in range(start_duty, end_duty - 1, -step):
            pin.ChangeDutyCycle(duty)
            time.sleep(0.1)

# Move forward
def forward(duration=1, final_speed=100):
    stop() 
    change_speed(pwm_objects['left'][0], 0, final_speed)
    change_speed(pwm_objects['right'][0], 0, final_speed)
    time.sleep(duration)
    stop()

# Move backward
def backward(duration=1, final_speed=100):
    stop() 
    change_speed(pwm_objects['left'][1], 0, final_speed)
    change_speed(pwm_objects['right'][1], 0, final_speed)
    time.sleep(duration)
    stop()

# Turn left
def turn_left(duration=1, final_speed=100):
    stop() 
    change_speed(pwm_objects['left'][1], 0, final_speed)
    change_speed(pwm_objects['right'][0], 0, final_speed)
    time.sleep(duration)
    stop()

# ПTurn right
def turn_right(duration=1, final_speed=100):
    stop() 
    change_speed(pwm_objects['left'][0], 0, final_speed)
    change_speed(pwm_objects['right'][1], 0, final_speed)
    time.sleep(duration)
    stop()

# Main function
def main():
    init()
    try:
        while True:
            command = input("Введите команду (forward, backward, left, right, stop): ").strip().lower()
            if command == "forward":
                forward()
            elif command == "backward":
                backward()
            elif command == "left":
                turn_left()
            elif command == "right":
                turn_right()
            elif command == "stop":
                stop()
            else:
                print("Неизвестная команда")
    except KeyboardInterrupt:
        print("Программа остановлена")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()