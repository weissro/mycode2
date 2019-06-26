#!/usr/env/python3



### import paramiko so we can talk to ssh
import paramiko
import os

##shortcut issuing commands to remote

def commandissue(command_to_issue):
    ssh_stdin,ssh_stdout,ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

#sshsession= paramiko.SSHClient()



def commander():
    commands = []
    x = 0

    while x == 0:
        whattodo = input("What command would you like to perform? ")
        commands.append(whattodo)
        cont = input("Would you like to enter another command? Please type y or n: ")
        if cont.lower == "y":
            print("I will input another command.\n")
            continue
        elif cont.lower == "n":
            print("I will not input more commands")
            x = x + 1;
        else:
            print("That was an invalid keystroke.  I will not issue any other commands")
            x = x + 1;
    return whattodo
    
sshsession = paramiko.SSHClient()

###if you want to connect using un / pw #####
#sshsession.connect(server, username=username, password=password)

#mykey is our private key
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

#if we never went to this SSH host, add the fingerprint to the known host file
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

## creds to connect
sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

##simple list of commands to issue across our connection
#our_commands =  ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]
#our_commands = commander()

## cycle through our commands and isssssssssssssssue them on the far end
#for x in our_commands:
#    print(commandissue(x).decode("utf-8"))

texter = commandissue(commander()).decode("utf-8")


print(texter)
