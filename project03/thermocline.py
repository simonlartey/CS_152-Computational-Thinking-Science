
'''
Simon Lartey,
09/28/2023,
CS 152B
this program computes the depth of thermocline on great pond
'''
import stats
#converts water temperatures into water densities
def density(temps):
	density_values = []
	for t in temps:
		rho = 1000 * (1 - (t + 288.9414) * (t - 3.9863)**2 / (508929.2*(t + 68.12963)))
		density_values.append(rho)
	return density_values	

#omputes the depth of the maximum change in density
def thermocline_depth(temps, depths):
    rhos = density(temps)
    drho_dz =[]
    for i in range(len(rhos) - 1):
        d_rho = rhos[i+1] - rhos[i] 
        d_z = depths[i+1] - depths[i]
        drho_dz.append(d_rho / d_z)
    
    max_drho_dz =  stats.maximum_data(drho_dz)   
    maxindex = stats.maximum_value_index(drho_dz)
	
    thermoDepth = ( depths[maxindex]+ depths[maxindex+1])/2
    
    return thermoDepth

#Compute the thermocline for each day in July
def main():
    fields = [10, 11, 16, 17, 15, 14, 13, 12]
    depths = [ 1, 3, 5, 7, 9, 11, 13, 15 ]

    ## open the data file and read past the header line
    file = open('GoldieJuly2019.csv','r')
    file.readline()
    	# assign to day the value 0
    day = 0
    # Open a file named “thermo_depths_july.csv” in write mode
    file_1 = open('thermo_depths_july.csv', 'w') 
    # Writing “day,depth” as a header to the file
    file_1.write('day, depth'+ "\n")
    
    	# for each line in the file, split the line on commas and assign it to words
    for line in file :
        words = line.split(",")
        if '12:03:00 PM' in words[0]:
            day+=1
            temps = []

        # loop over the number of items in depths (loop variable i)
        # append to temps the result of casting words[ fields[i] ] to a float    
            for items in range(len(depths)):
                temps.append(float(words[ fields[items] ]))
            thermo_depth = thermocline_depth(temps ,depths)
            file_1.write(str(day) + ","+ str(thermo_depth)+ "\n")

    file_1.close()
    file.close()

if __name__ == '__main__':
    main()