'''
    CPUTemp is a small program to print the temperature of cpu
    with the specified time delay in the following code.

'''

# "pip install gpiozero" if necessary

from gpiozero import CPUTemperature
import time

delay_seconds=10

while True:
    cpu=CPUTemperature()
    print(f"For {delay_seconds} seconds intreval, CPU Temperature is {cpu.temperature}")
    time.sleep(delay_seconds)