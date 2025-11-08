'''Simon Lartey
09/15/2023
CS152B
lab01'''

import random
import sys
import matplotlib.pyplot as plt

# Indices of list of parameters
IDXCalvingInterval = 0
IDXDartingProbability = 1
IDXJuvenileAge = 2
IDXMaximumAge = 3
IDXCalfSurvivalProbability = 4
IDXAdultSurvivalProbability = 5
IDXSeniorSurvivalProbability = 6
IDXCarryingCapacity = 7
IDXNumberOfYears = 8

# Indices to keep track of elephant features
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
    elephant = [0, 0, 0, 0]
    elephant[IDXGender] = random.choice(['m', 'f'])
    elephant[IDXAge] = age

    if elephant[IDXGender] == 'f' and parameters[IDXJuvenileAge] < elephant[IDXAge] <= parameters[IDXMaximumAge]:
        if random.random() < 1.0 / parameters[IDXCalvingInterval]:
            elephant[IDXMonthsPregnant] = random.randint(1, 22)
    elephant[IDXMonthsContraceptiveRemaining] = 0
    return elephant


def initPopulation(parameters):
    carrying_capacity = parameters[IDXCarryingCapacity]
    population = []
    for _ in range(carrying_capacity):
        age = random.randint(1, parameters[IDXMaximumAge])
        elephant = newElephant(parameters, age)
        population.append(elephant)
    return population


def incrementAge(population):
    for elephant in population:
        elephant[IDXAge] += 1
    return population


def calcSurvival(parameters, population):
    new_population = []

    for elephant in population:
        age = elephant[IDXAge]
        survival_probability = 0.0

        if age < parameters[IDXJuvenileAge]:
            survival_probability = parameters[IDXCalfSurvivalProbability]
        elif age < parameters[IDXMaximumAge]:
            survival_probability = parameters[IDXAdultSurvivalProbability]
        else:
            survival_probability = parameters[IDXSeniorSurvivalProbability]

        if random.random() < survival_probability:
            new_population.append(elephant)

    return new_population


def dartElephants(parameters, population):
    darting_probability = parameters[IDXDartingProbability]
    juvenile_age = parameters[IDXJuvenileAge]
    maximum_age = parameters[IDXMaximumAge]

    for elephant in population:
        gender = elephant[IDXGender]
        age = elephant[IDXAge]

        if gender == 'f' and juvenile_age < age <= maximum_age:
            if random.random() < darting_probability:
                elephant[IDXMonthsPregnant] = 0
                elephant[IDXMonthsContraceptiveRemaining] = 22

    return population


def cullElephants(parameters, population):
    carrying_capacity = parameters[IDXCarryingCapacity]
    num_elephants = len(population)
    num_culled = num_elephants - carrying_capacity

    if num_culled > 0:
        random.shuffle(population)
        new_population = population[:carrying_capacity]
    else:
        new_population = population

    return new_population, num_culled


def controlPopulation(parameters, population):
    percent_darted = parameters[IDXDartingProbability]

    if percent_darted == 0:
        newpop, numCulled = cullElephants(parameters, population)
    else:
        newpop = dartElephants(parameters, population)
        numCulled = 0

    return newpop, numCulled


def simulateMonth(parameters, population):
    calving_interval = parameters[IDXCalvingInterval]
    juvenile_age = parameters[IDXJuvenileAge]
    maximum_age = parameters[IDXMaximumAge]
    for e in population:
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


def simulateYear(parameters, population):
    population = calcSurvival(parameters, population)
    population = incrementAge(population)

    for _ in range(12):
        population = simulateMonth(parameters, population)

    return population


def calcResults(parameters, population, numCulled):
    juvenile_age = parameters[IDXJuvenileAge]
    max_age = parameters[IDXMaximumAge]
    num_calves = 0
    num_juveniles = 0
    num_adult_males = 0
    num_adult_females = 0
    num_seniors = 0

    for elephant in population:
        age = elephant[IDXAge]
        gender = elephant[IDXGender]
        if age == 1:
            num_calves += 1
        elif age <= juvenile_age:
            num_juveniles += 1
        elif juvenile_age <= age < max_age and gender == 'm':
            num_adult_males += 1
        elif juvenile_age <= age < max_age and gender == 'f':
            num_adult_females += 1
        elif age > max_age:
            num_seniors += 1

    total_population = len(population)
    results = [total_population, num_calves, num_juveniles, num_adult_males, num_adult_females, num_seniors, numCulled]
    return results


def runSimulation(parameters):
    popsize = parameters[IDXCarryingCapacity]
    population = initPopulation(parameters)
    population, numCulled = controlPopulation(parameters, population)

    results = []
    for i in range(parameters[IDXNumberOfYears]):
        population = simulateYear(parameters, population)
        population, numCulled = controlPopulation(parameters, population)
        results.append(calcResults(parameters, population, numCulled))
        if results[i][0] > 2 * popsize or results[i][0] == 0:
            print('Terminating early')
            break
    return results

results = runSimulation(parameters)

def sensitivityAnalysis(parameters):
    calf_survival_rates = [0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
    results_by_calf_survival = []

    for calf_survival_rate in calf_survival_rates:
        parameters[IDXCalfSurvivalProbability] = calf_survival_rate
        results = runSimulation(parameters)
        results_by_calf_survival.append((calf_survival_rate, results))

    plotSensitivityAnalysis(calf_survival_rates, results_by_calf_survival)


def plotSensitivityAnalysis(calf_survival_rates, results_by_calf_survival):
    total_population_avg = [result[0] for (calf_survival_rate, result) in results_by_calf_survival]
    num_calves_avg = [result[1] for (calf_survival_rate, result) in results_by_calf_survival]

    plt.figure(figsize=(10, 6))
    plt.plot(calf_survival_rates, total_population_avg, label="Average Total Population")
    plt.plot(calf_survival_rates, num_calves_avg, label="Average Number of Calves")
    plt.xlabel("Calf Survival Rate")
    plt.ylabel("Population Metrics")
    plt.title("Sensitivity Analysis: Calf Survival Rate")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    sensitivityAnalysis(parameters)
