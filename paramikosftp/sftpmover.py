#!/usr/bin/env python3
## Moving files with SFTP

import paramiko
import os

##where to connect to
t = paramiko.Transport("10.10.2.3", 22) ## IP and port)

##how to connect (see other labs)

t.connect(username="bender", password="alta3")
 
##Make SFTP connection object
sftp = paramiko.SFTPClient.from_transport(t)

##iterate across the files within the directory

for x in os.listdir("/home/student/filestocopy"): ##iterate on directory contents
    if not os.path.isdir("/home/student/filestocopy/"+x): #filter everything that is not a directory
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) #move file to target location

##close the connection
sftp.close()
print("Files moved to Bender. BITE MY SHINY METAL ASS!!!!")

