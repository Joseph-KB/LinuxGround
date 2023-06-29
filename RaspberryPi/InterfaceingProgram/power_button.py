'''
	This is a small code for installing a power button for shutdown 
	and reboot of raspberry pi.
	You need a pushbotton, Connect it to the below mentioned GPIO pin
'''
'''
	First create a python file with the below code in a specific folder
	and copy the path of the file. 

	Make this file an executeable file using the command
	"sudo chmod +x /path/of/this_file.py/"

	In the file /etc/rc.local, enter "/usr/bin/python3 /path/to
	/this_file.py" before the exit 0 line.

	Reboot the system. You are all set

'''




from gpiozero import Button
import subprocess


# Set up the button for power control
power_button = Button(3,hold_time=3)  # GPIO pin for power button

def shutdown():
    print("Shutting down...")
    subprocess.run(["sudo", "shutdown"])

def reboot():
    print("Rebooting.....")
    subprocess.run(["sudo", "shutdown","-r"])

# Define the button behavio
power_button.when_pressed = shutdown
power_button.when_held = reboot


# Keep the script running
while True:
    pass
