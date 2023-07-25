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

'''
	In Kali linux -kalipi - raspberryPi
	Check what all command combinations works
	pip install gpiozero
	sudo apt install python3-gpiozero

	groups kali 	-- to know whether gpiozero is in user group if not
	sudo groupadd gpio
	sudo chown root:gpio /dev/gpioemem
	sudo chmod g+rw /dev/gpiomem
	sudo usermod -aG gpio kali


	for enableing this power function after reboot do the following
	make a copy of the below code anywhere else and make it an executable file using chmod

	make another file power_on_switch.service in /etc/systemd/system
	In the file add the following
	
	[Unit]
	Description=PowerON_Off using Switch
	After=network.target

	[Service]
	ExecStart=/usr/bin/python3 /system_conf_files/power_button.py
	Restart=always
	User=root
	Group=root
	Type=simple

	[Install]
	WantedBy=multi-user.target


'''

from gpiozero import Button
import subprocess
import time


# Set up the button for power control
power_button = Button(3,hold_time=3)  # GPIO pin for power button

def shutdown():
    print("Shutting down...")
    subprocess.run(["sudo", "shutdown","-h"])

def reboot():
    print("Rebooting.....")
    subprocess.run(["sudo", "reboot"])
    time.sleep(15)

# Define the button behavio
power_button.when_pressed = shutdown
power_button.when_held = reboot

# Keep the script running
while True:
    pass
