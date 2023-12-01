from netmiko import ConnectHandler
import getpass
import os


# Obtain Username
username = input("Please enter your Username:")

# Obtain Password
password = getpass.getpass(prompt="Please enter your Password:")

# Current working Directory
current_dir = os.getcwd()

# Define Output Directory
output_dir = os.path.join(current_dir +'/output/')

print(output_dir)

# Define the filename for the devices file
devices_filename = "devices.txt"

# Define the show commands you want to execute on this device
commands = ['sh run | i hostname','sh run','sh int status','sh ip int bri','sh vlan','sh ver','sh inventory','sh mod','sh mac address-table','sh arp','sh cdp neighbors','sh ip protocols','sh ip route','sh vpc']

# Open the devices file and read the list of devices
with open(devices_filename, "r") as devices_file:
    devices = devices_file.read().splitlines()

# Loop through each device and execute the commands
for device in devices:
    print('Connecting to device:', device)

    # Define the netmiko parameters for SSH connection
    netmiko_params = {
    	"device_type": "cisco_ios",
    	"username": username,
    	"password": password,
	"ip": device,
    	"global_delay_factor": 2
    }

    # Establish the Netmiko connection
    with ConnectHandler(**netmiko_params) as net_connect:

        # Execute the commands and save the output to a file
        output_file = output_dir + device + '.txt'

        with open(output_file, 'w') as f:
            for command in commands:
                output = net_connect.send_command(command)
                print ('Executing ......', command)
                f.write(f'{command}\n{output}\n')
