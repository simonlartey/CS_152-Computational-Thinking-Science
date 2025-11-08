'''Simon Lartey
09/15/2023
CS152B
lab01'''

import random
import sys
#indices of list of parameters
IDXCalvingInterval = 0
IDXDartingProbability = 1
IDXJuvenileAge = 2
IDXMaximumAge = 3
IDXCalfSurvivalProbability = 4
IDXAdultSurvivalProbability = 5
IDXSeniorSurvivalProbability = 6
IDXCarryingCapacity = 7
IDXNumberOfYears = 8


# indices to keep track of elephant features
IDXGender = 0
IDXAge = 1
IDXMonthsPregnant = 2
IDXMonthsContraceptiveRemaining = 3

calving_interval = 3.1
darting_probability = 0.0
juvenile_age = 12
maximum_age = 60
calf_survival_probability = 0.85
adult_survival_probability = 0.996
senior_survival_probability = 0.20
carrying_capacity = 7000
number_of_years = 200

parameters = [
    calving_interval,
    darting_probability,
    juvenile_age,
    maximum_age,
    calf_survival_probability,
    adult_survival_probability,
    senior_survival_probability,
    carrying_capacity,
    number_of_years
    ]



def newElephant(parameters, age):


    # Initialize an elephant list with default values
    elephant = [0, 0, 0, 0]

    # Assign a random gender to the elephant
    elephant[IDXGender] = random.choice(['m', 'f'])

    # Assign the provided age to the elephant
    elephant[IDXAge] = age

    # Check if the elephant is female and within breeding age
    if elephant[IDXGender] == 'f' and parameters[IDXJuvenileAge] < elephant[IDXAge] <= parameters[IDXMaximumAge]:
        # Test if the elephant is pregnant based on calving interval
        if random.random() < 1.0 / parameters[IDXCalvingInterval]:
            # Assign a random number of months (1 to 22) to represent pregnancy
            elephant[IDXMonthsPregnant] = random.randint(1, 22)
    elephant[IDXMonthsContraceptiveRemaining] = 0
    # Return the elephant list
    return elephant

# This function creates a list of elephants based on the provided parameters.
def initPopulation(parameters):
    carrying_capacity = parameters[IDXCarryingCapacity]
    population = []
    for elephant in range(parameters[IDXCarryingCapacity]):
        age = random.randint(1, parameters[IDXMaximumAge])
        elephant = newElephant(parameters, age)
        population.append(elephant)
    return population

# This function iterates through the population list and increases the age of each elephant by one year.
def incrementAge(population):
    for elephant in range(len(population)):
        population [elephant][IDXAge] += 1
    return population

# This function evaluates the survival probability for each elephant in the population
def calcSurvival(parameters, population):
    new_population = []

    for elephant in population:
        age = elephant[IDXAge]
        survival_probability = 0.0

        if age < parameters[IDXJuvenileAge]:
            # Calf survival
            survival_probability = parameters[IDXCalfSurvivalProbability]
        elif age < parameters[IDXMaximumAge]:
            # Adult survival
            survival_probability = parameters[IDXAdultSurvivalProbability]
        else:
            # Senior survival
            survival_probability = parameters[IDXSeniorSurvivalProbability]

        # Check if the elephant survives based on the calculated probability
        if random.random() < survival_probability:
            new_population.append(elephant)

    return new_population

# This function evaluates the darting probability for female elephants
def dartElephants(parameters, population):
    darting_probability = parameters[IDXDartingProbability]
    juvenile_age = parameters[IDXJuvenileAge]
    maximum_age = parameters[IDXMaximumAge]

    for elephant in population:
        gender = elephant[IDXGender]
        age = elephant[IDXAge]

        # Check if the elephant is a female, older than the juvenile age, and younger than the maximum age
        if gender == 'f' and juvenile_age < age <= maximum_age:
            # Determine if the elephant should be darted based on the darting probability
            if random.random() < darting_probability:
                # If darted, reset the pregnancy and set months of contraceptive remaining to 22
                elephant[IDXMonthsPregnant] = 0
                elephant[IDXMonthsContraceptiveRemaining] = 22

    return population

# This function evaluates the number of elephants that need to be culled
def cullElephants(parameters, population):
    carrying_capacity = parameters[IDXCarryingCapacity]
    num_elephants = len(population)

    # Calculate the number of elephants that need to be culled
    num_culled = num_elephants - carrying_capacity

    # If there are too many elephants, shuffle the population list and keep the first carrying_capacity elephants
    if num_culled > 0:
        random.shuffle(population)
        new_population = population[:carrying_capacity]
    else:
        # If there are not too many elephants, no culling is needed
        new_population = population

    # Return the new population and the number of elephants culled
    return new_population, num_culled

# This function determines whether elephants should be darted based on
def controlPopulation(parameters, population):
    percent_darted = parameters[IDXDartingProbability]

    if percent_darted == 0:
        newpop, numCulled = cullElephants(parameters, population)
    else:
        newpop = dartElephants(parameters, population)
        numCulled = 0

    return newpop, numCulled

# This function simulates various changes in the elephant population over
def simulateMonth(parameters, population):
    calving_interval = parameters[IDXCalvingInterval]
    juvenile_age = parameters[IDXJuvenileAge]
    maximum_age = parameters[IDXMaximumAge]
    for e in population:
    #for idx in range(len(population)):
    #    e = population[idx]
        gender = e[IDXGender]
        age = e[IDXAge]
        monthsPregnant = e[IDXMonthsPregnant]
        monthsContraceptive = e[IDXMonthsContraceptiveRemaining]

        if gender == 'f' and juvenile_age < age <= maximum_age:
            if monthsContraceptive > 0:
                e[IDXMonthsContraceptiveRemaining] -= 1
            elif monthsPregnant > 0:
                if monthsPregnant >= 22:
                    new_calf = newElephant(parameters, age=1)
                    population.append(new_calf)
                    e[IDXMonthsPregnant] = 0
                else:
                    e[IDXMonthsPregnant] += 1
            elif random.random() < (1.0 / (calving_interval * 12 - 22)):
                e[IDXMonthsPregnant] = 1

    return population


# This function simulates various changes in the elephant population over a
def simulateYear(parameters, population):
    # Call calcSurvival
    population = calcSurvival(parameters, population)

    # Call incrementAge
    population = incrementAge(population)

    # Loop through 12 months, calling simulateMonth
    for i in range(12):
        population = simulateMonth(parameters, population)

    # Return the updated population after the year simulation
    return population

# This function calculates various statistics related to the elephant population,
def calcResults(parameters, population, numCulled):
    # Get the juvenile age and max age parameters
    juvenile_age = parameters[IDXJuvenileAge]
    max_age = parameters[IDXMaximumAge]

    # Initialize variables to hold the number of each category
    num_calves = 0
    num_juveniles = 0
    num_adult_males = 0
    num_adult_females = 0
    num_seniors = 0

    # Loop over the population list and categorize each elephant
    for elephant in population:
        age = elephant[IDXAge]
        gender = elephant[IDXGender]
        if age == 1:
            num_calves += 1
        elif age <= juvenile_age:
            num_juveniles += 1
        elif juvenile_age <= age <= max_age and gender == 'm':
            # Increment num_juveniles when age is in the juvenile range
            num_adult_males += 1
        elif juvenile_age <= age <=max_age and gender == 'f':
            num_adult_females += 1
        elif age > max_age:
            num_seniors += 1

    # Calculate the total population size
    total_population = len(population)
    results = [total_population, num_calves,num_juveniles,num_adult_males, num_adult_females,num_seniors,numCulled]
    return results 


# This function initiates the simulation, running it for the specified number of
def runSimulation(parameters):
    popsize = parameters[IDXCarryingCapacity]

    # Initialize the population
    population = initPopulation(parameters)
    population, numCulled = controlPopulation(parameters, population)

    # Run the simulation for N years, storing the results
    results = []
    for i in range(parameters[IDXNumberOfYears]):
        population = simulateYear(parameters, population)
        population, numCulled = controlPopulation(parameters, population)
        results.append(calcResults(parameters, population, numCulled))
        if results[i][0] > 2 * popsize or results[i][0] == 0:
            # Cancel early, out of control
            print('Terminating early')
            break
    
    return results


def main(argv):
    if len(argv) < 2:
        print("Usage: python your_script.py <darting_probability>")
        sys.exit(1)

    # Parse the darting probability from the command line argument
    probDart = float(argv[1])

    # Create the parameter list
    parameters = [
        calving_interval,
        probDart,  # Use the provided darting probability
        juvenile_age,
        maximum_age,
        calf_survival_probability,
        adult_survival_probability,
        senior_survival_probability,
        carrying_capacity,
        number_of_years
    ]

    # Run the simulation and store the results
    results = runSimulation(parameters)
    print(results[-1])

    # Calculate and print the average results
    num_simulations = len(results)
    total_population_avg = sum(result[0] for result in results) / num_simulations
    num_calves_avg = sum(result[1] for result in results) / num_simulations
    num_juveniles_avg = sum(result[2] for result in results) / num_simulations
    num_adult_males_avg = sum(result[3] for result in results) / num_simulations
    num_adult_females_avg = sum(result[4] for result in results) / num_simulations
    num_seniors_avg = sum(result[5] for result in results) / num_simulations

    print(f"Current Darting Probability: {probDart}")
    print("Average Results:")
    print(f"Average Total Population: {total_population_avg:.2f}")
    print(f"Average Number of Calves: {num_calves_avg:.2f}")
    print(f"Average Number of Juveniles: {num_juveniles_avg:.2f}")
    print(f"Average Number of Adult Males: {num_adult_males_avg:.2f}")
    print(f"Average Number of Adult Females: {num_adult_females_avg:.2f}")
    print(f"Average Number of Seniors: {num_seniors_avg:.2f}")
if __name__ == "__main__":
    main(sys.argv)






