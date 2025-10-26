"""
temps.py

Simon Lartey
Fall 2023
CS152 project 2

This program calculates the highest and lowest air temperature,
and also the highest and lowest water temperature.

"""

GoldieMLRCJuly = open("GoldieMLRCJuly.csv","r")
high_air_temp = -200
low_air_temp = 1000

high_water_temp = -200
low_water_temp = 1000

header_line = GoldieMLRCJuly.readline()
for line in GoldieMLRCJuly:
    words = line.split(",")
    air_temp = float(words[5])
    water_temp = float(words[1])
    

    # finding the highest air temperature
    if air_temp > high_air_temp:
        high_air_temp = air_temp
        

    #finding the highest water temperature
    if water_temp> high_water_temp:
        high_water_temp = water_temp
        

    #finding the lowest air temperature
    if air_temp < low_air_temp:
        low_air_temp = air_temp
       

    #finding the lowest water tempereture
    if water_temp < low_water_temp:
        low_water_temp = water_temp
        
print("Highest air Temp: %7.3f" % (high_air_temp))
print("Highest water Temp: %7.3f" % (high_water_temp))
print("Lowest air Temp: %7.3f" % (low_air_temp))
print("Lowest water Temp: %7.3f" % (high_water_temp))
