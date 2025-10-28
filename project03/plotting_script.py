'''Ike Lage
09/20/2023
CS 152 B
Project 3
This is a program to generate a plot of the thermocline depth for each day in July
It assumes the file where this data is stored is named thermo_depths_july.csv;
the file has 1 header line; it is in the same directory as this script; 
the first column is the day number, and the second column is the themocline depth at noon on that day;
the 2 columns are separated by commas.  Each day is on its own line/
'''

import pylab as plt

##Open up the file you wrote in the first part of T7
file_name = open( 'thermo_depths_july.csv' )

##Read the header line.  This isn't data to plot.
##Reading it here means it won't be the first 
##line in the for loop
header_line = file_name.readline()

##Make 2 lists to collect the day numbers and the thermocline_depths
days = []
thermo_depths = []

for line in file_name:

    ##Split apart the 2 columns in the line
    line = line.split( ',' )
    
    ##Add the data in the first column to the days list as an int
    days.append( int( line[ 0 ].strip() ) )

    ##Add the data in the second column to the thermocline_depths list as an float
    thermo_depths.append( float( line[ 1 ].strip() ) )

##Plot days by temperatures
plt.scatter( days , thermo_depths , color='b' , marker='x' )

##Add title/axes labels etc to the plot
plt.title( 'Thermocline depth at noon for each day in July' )
plt.xlabel( 'Day in July' )
plt.ylabel( 'Thermocline Depth at Noon' )
	
##Save, then show the plot
plt.savefig( 'thermo_depth_by_day_in_july.png' , bbox_inches='tight' )
plt.show()
