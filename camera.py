import time
import Jetson.GPIO as GPIO
from datetime import datetime

FPS = 1
output_pin = 16

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.HIGH
    
    try:
        while True:
            time.sleep((1/FPS)/2)
            GPIO.output(output_pin, curr_value)
            curr_value ^= GPIO.HIGH
            #if curr_value == 1:
            print(datetime.now(), "Outputting {} to pin {}".format(curr_value, output_pin))
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
