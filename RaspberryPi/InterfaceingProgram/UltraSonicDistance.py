'''
    Working voltage of Ultra sonic sensor is 5Volt DC voltage
    "HC-SR04"
    This is the program to find the length of an object from
    the tip of UltraSonic Sensor
    Ensure that the GPIO's are correctly connected


'''

import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pins
GPIO.setmode(GPIO.BCM)
TRIG_PIN = 23
ECHO_PIN = 24

def measure_distance():
    # Set up the GPIO pins
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

    # Send a short pulse to trigger the ultrasonic sensor
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # Measure the time it takes for the pulse to return
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()

    # Calculate the distance based on the time difference
    pulse_duration = pulse_end - pulse_start
    speed_of_sound = 34300  # centimeters per second
    distance = (speed_of_sound * pulse_duration) / 2
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = measure_distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()






"""
from gpiozero import DistanceSensor
import time

# Set up the ultrasonic sensor
sensor = DistanceSensor(echo=24, trigger=23)

def measure_distance():
    # Wait for the sensor to settle
    time.sleep(0.5)

    # Measure the distance
    distance = sensor.distance

    return distance

# Call the function to measure the distance
while True:
    distance = measure_distance()
    print(f"Distance: {distance:.2f} meters")

"""
