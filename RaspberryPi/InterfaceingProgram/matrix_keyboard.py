'''
    Below code is for printing characters in a matrix keyboard. Ensure the connection before
    turing on the machine. Simple connection from left to right view of matrix keyboard is shown below.
    
    
    If keypad is held on reading psition the corersponding eight wires are connected as mentioned below.

    |   |   |   |   |   |   |   |

    5   6   13  19  12  16  20  21
'''



import RPi.GPIO as GPIO
import time


lines=[5,6,13,19]
column=[12,16,20,21]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for i in lines:
    GPIO.setup(i,GPIO.OUT)
for i in column:
    GPIO.setup(i,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(column[0]) == 1):
        print(characters[0])
    if(GPIO.input(column[1]) == 1):
        print(characters[1])
    if(GPIO.input(column[2]) == 1):
        print(characters[2])
    if(GPIO.input(column[3]) == 1):
        print(characters[3])
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        readLine(lines[0], ["1","2","3","A"])
        readLine(lines[1], ["4","5","6","B"])
        readLine(lines[2], ["7","8","9","C"])
        readLine(lines[3], ["*","0","#","D"])
        time.sleep(0.25)
except KeyboardInterrupt:
    print("\nApplication stopped!")
