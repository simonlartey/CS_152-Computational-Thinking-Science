'''TODO: Simon Lartey
TODO: 09/20/2023
CS 152 B
Project 1
This is a program to simulate a disease using an SIR model
TODO: Description of what the program lets you do
'''

import pylab as plt

def simulate_SIR( S0 , I0 , R0 , n_days , num_spreading_contacts , recovery_time , population_size ):
	'''This function runs the SIR simulation for n_days given the initial sizes of the S/I/R groups (i.e. S0, I0, R0)
		and the parameters: num_spreading_contacts and recovery_time.  It returns 3 lists containing 
		the sizes of S, I and R over time.'''

	##Initialize the lists we'll use to collect the sizes of S/I/R over time
	S_list = []
	I_list = []
	R_list = []

	##initialize variables we'll need to use in the loop
	St = S0
	It = I0
	Rt = R0

	##Run the simulation for n_days
	for t in range( n_days ):

		##Compute the new values for S/I/R.  Make sure to use the old values of S/I/R throughout instead of the updated ones.
		St_new = compute_new_susceptible( num_spreading_contacts , St , It , population_size )
		It_new = compute_new_infected( num_spreading_contacts , recovery_time , St , It , population_size )
		Rt_new = compute_new_recovered( recovery_time , Rt , It )

		##Update St/It/Rt with the new sizes
		St = St_new
		It = It_new
		Rt = Rt_new

		##Add the sizes to the respective lists
		S_list.append( St )
		I_list.append( It )
		R_list.append( Rt )

	##Return the lists of simulation results
	return S_list , I_list , R_list

def plot_SIR( S_list , I_list , R_list , S0 , I0 , R0 ):
	'''This function plots the simulation data and saves the plot to the file sir_plot.png'''

	##Get a list of the number of days to use in the plot
	days_list = [ i for i in range( len( S_list ) ) ]

	##Plot the sizes of S, I and R over time
	plt.plot( days_list , S_list , color='b' , marker='x' )
	plt.plot( days_list , I_list , color='orange' , marker='o' )
	plt.plot( days_list , R_list , color='g' , marker='v' )

	##Add title/axes labels etc to the plot
	plt.title( 'SIR simulation for S0: ' + str( S0 ) + ", I0: " + str( I0 ) + ", R0: " + str( R0 ) )
	plt.xlabel( '# Days' )
	plt.ylabel( '# people' )
	plt.legend( [ 'Susceptible' , 'Infected' , 'Recovered' ] )
	
	##Save, then show the plot
	plt.savefig( 'sir_plot.png' , bbox_inches='tight' )
	plt.show()


##TODO: This is where your compute_new_susceptible function should go
def compute_new_susceptible(num_spreading_contacts, S0, I0 , population_size):
    S1= S0 - num_spreading_contacts * I0*S0/population_size 
    return S1 
##This is your compute_new_infected function
def compute_new_infected( num_spreading_contacts, recovery_time, S0, I0 , population_size ):
	##Complete the function compute_new_infected
   I1 = I0 + num_spreading_contacts * I0 * S0/population_size  - I0/recovery_time  
   return I1 

##This is your compute_new_recovered function
def compute_new_recovered( recovery_time , R0 , I0 ):
	R1= R0+I0/recovery_time
	return R1
	##Complete the function compute_new_recovered


##TODO: This is where your compute_population_size function should go


def compute_population_size(S0,I0,R0):
    return(S0+I0+R0)

##Set the number of days to 100
n_days = 100

##TODO: This is where you should get the user input to get the parameters S0 , I0 , R0 
S0=int(input("Enter the S0 for the similation: "))
I0=int(input("Enter the I0 for the simulation: "))
R0=int(input("Enter the R0 for the simulation: "))



##TODO: This is where you should compute the population size

population_size= compute_population_size(S0,I0,R0)

##TODO: THis is where you should get the user input to get the parameters num_spreading_contacts , recovery_time

num_spreading_contacts=float(input("Enter NS for number of spreading contact: "))
recovery_time=float(input("Enter RT for recovery time: "))

##TODO: This is where you should compute S1

S1 = compute_new_susceptible( num_spreading_contacts , S0 , I0 , population_size )
print( "S1=", S1 )
##TODO: This is where you should compute R1 
R1=compute_new_recovered(recovery_time, R0, I0)
print("R1=",R1)

##TODO: This is where you should compute I1
I1=compute_new_infected(num_spreading_contacts, recovery_time, S0, I0, population_size)
print("R1=",R1)

##TODO: This is where your call to the simulation function, then the plotting function should go
S_list , I_list , R_list = simulate_SIR( S0 , I0 , R0 , n_days , num_spreading_contacts , recovery_time , population_size )
plot_SIR( S_list , I_list , R_list , S0 , I0 , R0 )

