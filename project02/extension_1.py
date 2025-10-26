"""
extension_1.py

Simon Lartey
Fall 2023
CS152 project 2

This program calculates the average wind speed for day by looping through the 
lines to calculate the number of readings and the total wind speed.

"""


# opening and reading the file
fp = open( "GoldieMLRCJuly.csv", "r" )
lines = fp.readlines()

#Initializing variables
no_readings =0
readings_per_day = 96
total_wind_speed = 0 
currrent_day = 1
#Looping through the lines to calculate the number of readings and total wind speed
for line in lines[1:]:
    no_readings += 1

    words = line.split(",")
    wind_speed = float(words[6])
    total_wind_speed += wind_speed

#Calculating average wind speed for the day
    if no_readings == 96:
        average_wind_speed = total_wind_speed / readings_per_day
        print("average wind speed for day",currrent_day,average_wind_speed)
        no_readings = 0 
        total_wind_speed = 0
        currrent_day += 1