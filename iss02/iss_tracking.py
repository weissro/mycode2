#!/usr/bin/env python3

import urllib.request
import json
import turtle
import time

##Trace the ISS - earth orbital space station
eoss = "http://api.open-notify.org/iss-now.json"

#call the webserv
trackiss = urllib.request.urlopen(eoss)

##put into file object
ztrack = trackiss.read()

##json 2 python data structure
result = json.loads(ztrack.decode("utf-8"))

##display our pythonic data
print("\nConverted python data")
print(result)
input("\nISS data retrieved and converted.  Press any key to continue")

location = result["iss_position"]
lat = location["latitude"]
lon = location["longitude"]
print("\nLatitude: ", lat)
print("Longitude: ", lon)

screen = turtle.Screen() #create a screen object
screen.setup(720,360) # set the resolution

screen.setworldcoordinates(-180,-90,180,90)

screen.bgpic("iss_map.gif")

screen.register_shape("spriteiss.gif")
iss = turtle.Turtle()
iss.shape("spriteiss.gif")
iss.setheading(90)
lon = round(float(lon))
lat = round(float(lat))

##My location
yellowlat = 33.30
yellowlon = -96.99
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color("yellow")
mylocation.goto(yellowlon,yellowlat)
mylocation.dot(5)
mylocation.hideturtle()


#iss.penup()
#iss.goto(lon,lat)


passiss = "http://api.open-notify.org/iss-pass.json"
passiss = passiss + "?lat=" + str(yellowlat) + "&lon=" + str(yellowlon)
response = urllib.request.urlopen(passiss)
result = json.loads(response.read().decode("utf-8"))
## print(result) #uncomment to see downloaded result

over = result["response"][1]["risetime"]
style = ("Arial", 6, "bold")
mylocation.write(time.ctime(over),font=style)

iss.penup()
iss.goto(lon,lat)



turtle.mainloop() #this has to be at the bottom to prevent graphic from closing

