'''simon lartey
CS152 B
10/19/2023
'''


# Import the necessary libraries, including Matplotlib for plotting
import random
import sys
import matplotlib.pyplot as plt

# Define a function to initialize the population with a given size and female probability.
def  initPopulation(N, probFemale):
    # Initialize an empty list to store the population
    population = []
    for i in range(N):
        # Generate a random number between 0 and 1.
        gen_random = random.random()
        if gen_random<probFemale:
            # Add 'f' for female if the random number is less than probFemale, else add 'm' for male.
            population.append('f')
        else:
            population.append('m')
            # Return the initialized population list.
    return population

    

# Define a function to simulate a year's population growth based on various parameters.
def simulateYear(pop,elNinoProb,stdRho,elNinoRho,probFemale,maxCapacity):
    # Initialize a variable to track whether it's an El Nino year.
    elNinoYear = False

    if random.random() < elNinoProb:
        elNinoYear = True # Set elNinoYear to True with a certain probability.

# Initialize a new list to store the population after a year's simulation
    newpop = []
    for peng in pop:
        if len(newpop) >= maxCapacity:
            break   # Stop adding to the new population if it reaches the maximum capacity.


        if elNinoYear:
            if random.random() < elNinoRho:
                newpop.append(peng)
        else:
            newpop.append(peng)
            if random.random() < (stdRho - 1.0):
                if random.random() < probFemale:
# Add female penguins with a certain probability during a non-El Nino year.
                    newpop.append('f')
                else:
                    newpop.append('m')
    return newpop



# Define a function to run a multi-year simulation of penguin population
def runSimulation(N,initPopSize,probFemale,elNinoProb,stdRho,elNinoRho,maxCapacity, minViable):
    population = initPopulation(initPopSize,probFemale)
    endDate = N
    for year in range(N):
        newPopulation = simulateYear(population, elNinoProb, stdRho, elNinoRho, probFemale,maxCapacity)
        

#check for validity
        
        if len(population) < minViable or ('f' not in newPopulation) or ('m' not in newPopulation) :
            endDate = year
            break
        population = newPopulation
        #print(f"Year {year+1}: Population size = {len(population)}")
    return endDate

#Initialize a list of zeros to store CEPD values.
def computeCEPD(simResult, N):
    CEPD = [0] * N

    for i in range(len(simResult)):
        if simResult[i] < N:
            for j in range(simResult[i], len(CEPD)):
                # Increment CEPD values for each year of the simulation.

                CEPD[j] += 1

    for year in range(len(CEPD)):
        CEPD[year] = CEPD[year] / len(simResult)
    return CEPD

# Main function for running the simulation and displaying results.
def main(argv):
    if len(argv) < 3:
        print("Error: Insufficient Arguments")
        exit()
    numSim = int(argv[1])
    yearsBetweenElNino = int(argv[2])
    N = 201
    initPopSize = 500
    probFemale = 0.5
    elNinoProb = 1.0 / yearsBetweenElNino
    stdRho = 1.188
    elNinoRho = 0.41
    maxCapacity = 2000
    minViable = 10
    runSimulationResults = []
    #Number_Results = 0

    for i in range(numSim):
        runSimulationResults.append(runSimulation(N, initPopSize, probFemale, elNinoProb, stdRho, elNinoRho, maxCapacity, minViable))
    Number_Results = 0
    for result in runSimulationResults:
        if result < N:
     # Count the number of simulations that resulted in a population surviving for less than N years.
            Number_Results += 1
    
    
    probSurvival = (Number_Results / numSim)
    print('Probability of survival after', N, 'years is', probSurvival)
    compCEPDresult = computeCEPD(runSimulationResults, N)

    for j in range(len(compCEPDresult)):
        if j % 10 == 0:
    #Display CEPD values at intervals of 10 years.
            print("In", j, "CEPD is", compCEPDresult[j])

    
    x = range(0, N)
    y = compCEPDresult
    plt.plot(x, y, '-')
    plt.title('CEPD with El Nino Cycles ')
    plt.xlabel('Year')
    plt.ylabel('CEPD')
    plt.show()

if __name__ == "__main__":
    main(sys.argv)
