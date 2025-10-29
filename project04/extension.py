'''simon lartey
CS152 B
10/19/2023
'''
import random
import pylab
import sys

# Initialize a population of penguins with specified gender probabilities
def  initPopulation(N, probFemale):
    population = []
    for i in range(N):
        gen_random = random.random()
        if gen_random<probFemale:
            population.append('f')# Female penguin
        else:
            population.append('m')# Male penguin
    return population

# Simulate a year in the penguin population with El Nino events
def simulateYear(pop,elNinoProb,stdRho,elNinoRho,probFemale,maxCapacity):
    
    elNinoYear = False
# Determine if it's an El Nino year based on the specified probability
    if random.random() < elNinoProb:
        elNinoYear = True

    newpop = []
    for peng in pop:
 # Stop simulating if the population exceeds the maximum capacity

        if len(newpop) >= maxCapacity:
            break

        if elNinoYear:
         # Determine penguin survival during El Nino based on elNinoRho
            if random.random() < elNinoRho:
                newpop.append(peng)
        else:
            newpop.append(peng)
            if random.random() < (stdRho - 1.0):
                if random.random() < probFemale:
                    newpop.append('f')# Penguins survive without El Nino
                else:
                    newpop.append('m') # Male penguin birth
    return newpop

# Run a simulation for a specified number of years and check for population validity

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
# Compute the Cumulative Extinction Probability Distribution (CEPD) based on simulation results
def computeCEPD(results, NSim):
    N = max(results) + 1
    CEPD = [0] * N  # Create a list of N zeros

    for extinction_year in results:
        for year in range(extinction_year, N):
            CEPD[year] += 1

    for year in range(N):
        CEPD[year] /= NSim

    return CEPD
def main():
    NSim = 100  # Number of simulations for each El Nino cycle
    initPopSize = 500
    probFemale = 0.5
    stdRho = 1.188
    maxCapacity = 2000
    elNinoRho = 0.41
    minViable = 10
    N = 201
    x_values = list(range(1, N + 1))

    elNinoCycles = [3, 5, 7]
    colors = ['b', 'g', 'r']
    labels = [f"El Nino Cycle {cycle} years" for cycle in elNinoCycles]

    for i, elNinoCycle in enumerate(elNinoCycles):
        elNinoProb = 1.0 / elNinoCycle
        result_list = []
        # Run simulations and store extinction years
        for simulation in range(NSim):
            year_of_extinction = runSimulation(N, initPopSize, probFemale, elNinoProb, stdRho, elNinoRho, maxCapacity, minViable)
            result_list.append(year_of_extinction)

        CEPD = [0] * N
        for extinction_year in result_list:
            for year in range(extinction_year, N):
                CEPD[year] += 1

        for year in range(N):
            CEPD[year] /= NSim

        # Plot the CEPD for the current El Nino cycle
        pylab.plot(x_values, CEPD, color=colors[i], label=labels[i])

    pylab.title("CEPD with Different El Nino Cycles")
    pylab.xlabel("Year")
    pylab.ylabel("CEPD")
    pylab.legend()
    pylab.savefig("CEPD_Plots.png")
    pylab.show()

if __name__ == "__main__":
    main()
