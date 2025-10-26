"""
sunny.py

Simon Lartey
Fall 2023
CS152 project 2

This program calculates the number of sunny and cloudy days and 
their corresponding averages.
"""

def main():
    
    #open and read GoldieMLRCJuly.csv
    fp = open( "GoldieMLRCJuly.csv", "r" )
    lines = fp.readlines()
    sunny_counter = 0
    cloudy_counter = 0
    sunny_total = 0
    cloudy_total = 0

    #loop through lines to find 12:03:00
    for line in lines[1:]:
        words = line.split(",")
        date_time = words[0]
        if "12:03:00 PM" in date_time:
            PAR = int(words[4])

            if PAR > 800:
                sunny_counter += 1
                sunny_total += PAR

    
            else:
                cloudy_counter += 1
                cloudy_total += PAR

    print("number of sunny days : " , sunny_counter)  
    print("number of cloudy days : " , cloudy_counter)  
    print("average number of sunny days : " , sunny_total/sunny_counter)  
    print("average number of cloudy days : " , cloudy_total/cloudy_counter)  

        #find the minimum PAR value
    fp = open( "GoldieMLRCJuly.csv", "r" )
    lines = fp.readlines()
    for line in lines[1:]:
        words = line.split(",")
        PAR = words[4]
        minimum_PAR = min(PAR)
    print("minimum PAR value : " , minimum_PAR)

if __name__ == "__main__":
	main()


   