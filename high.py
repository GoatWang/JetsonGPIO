import time
import Jetson.GPIO as GPIO
from datetime import datetime

output_pin = 16

def main():
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    while True:
        print(datetime.now())
        time.sleep(1)

if __name__ == '__main__':
    main()
