# Imports 
import RPi.GPIO as GPIO
import time
import sys

# Configuring GPIO pin numbers for motor control
motor_pins = {'left': (17, 18), 'right': (22, 23)}

# GPIO initailisation
def init():
    GPIO.setmode(GPIO.BCM)
    for pin_pair in motor_pins.values():
        for pin in pin_pair:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

# Stopping all motors
def stop():
    for pin_pair in motor_pins.values():
        for pin in pin_pair:
            GPIO.output(pin, False)

# Move forward
def forward(duration=1):
    GPIO.output(motor_pins['left'][0], True)
    GPIO.output(motor_pins['right'][0], True)
    time.sleep(duration)
    stop()

# Move backward
def backward(duration=1):
    GPIO.output(motor_pins['left'][1], True)
    GPIO.output(motor_pins['right'][1], True)
    time.sleep(duration)
    stop()

# Turn left
def turn_left(duration=1):
    GPIO.output(motor_pins['left'][1], True)
    GPIO.output(motor_pins['right'][0], True)
    time.sleep(duration)
    stop()

# ПTurn right
def turn_right(duration=1):
    GPIO.output(motor_pins['left'][0], True)
    GPIO.output(motor_pins['right'][1], True)
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
