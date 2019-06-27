#!/usr/bin/env python3

from netmiko import ConnectHandler

def bootstrapper(dev_type, dev_ip, dev_un, dev_pw, config):
    try:
        config_file = open(config, 'r') # Open the file object described in the config argument
        config_lines = config_file.read().splitlines() #create a list of the file lines without \n
        config_close.close() # close the file object

        open_connection = ConnectionHandler(device_type=dev_type, ip=dev_ip, \
                username=dev_un, password=dev_pw)
        open_connection.enable() #this sets the connection in enable mode
        output = open_connection.send_config_set(config_lines)
        print(output) #print the config to screen # ouput to the screen
        open_connection.send_command_expect('write memory')  # write the memory
        open_connection.disconnect() # close the open connection

        return True # everything worked!  - 
    except:
        return False

