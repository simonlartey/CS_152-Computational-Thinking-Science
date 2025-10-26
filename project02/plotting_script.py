'''Ike Lage
09/20/2023
CS 152 B
Project 2
This is a program to generate a plot of the air temp for each day in July at 3 pm 
It assumes the file where this data is stored is named Goldie2019July3PMAirTemp.csv;
the file has 1 header line; it is in the same directory as this script; 
the first column is the day number, and the second column is the air temp at 3 PM on that day;
the 2 columns are separated by commas
'''

import pylab as plt

##Open up the file you wrote in the first part of T7
file_name = open( 'Goldie2019July3PMAirTemp.csv' )

##Read the header line.  This isn't data to plot.
##Reading it here means it won't be the first 
##line in the for loop
header_line = file_name.readline()

##Make 2 lists to collect the day numbers and the temperature
days = []
temps = []

for line in file_name:

    ##Split apart the 2 columns in the line
    line = line.split( ',' )
    
    ##Add the data in the first column to the days list as an int
    days.append( int( line[ 0 ].strip() ) )

    ##Add the data in the second column to the temps list as an float
    temps.append( float( line[ 1 ].strip() ) )

##Plot days by temperatures
plt.scatter( days , temps , color='b' , marker='x' )

##Add title/axes labels etc to the plot
plt.title( 'Temperature at 3 PM for each day in July' )
plt.xlabel( 'Day in July' )
plt.ylabel( 'Temp at 3 PM' )
	
##Save, then show the plot
plt.savefig( 'temp_by_day_in_july.png' , bbox_inches='tight' )
plt.show()