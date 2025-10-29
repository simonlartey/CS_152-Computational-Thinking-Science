'''
simon lartey
10/12/2023
CS152B
'''
# Import the 'random' and 'pylab' modules for generating random numbers and plotting.
import random
import pylab
# Define a function 'gen_random' that generates a list of N random floating-point numbers between 0 and 1
def gen_random(N):
    numbers =[]
    for i in range(N):
        numbers.append(random.random())
    return numbers

# Define a test function 'test' to demonstrate the 'gen_random' function.
def test():
    random_numbers = gen_random(10)  # Generate a list of 10 random numbers.
    print(random_numbers)
test()

# Define a function 'genNintegersN' that generates a list of N random integers within a specified range [lowerBound, upperBound]
def genNintegersN(N,lowerBound,upperBound):
    numbers =[]
    for i in range(N):
        sorted_number = random.randint(lowerBound,upperBound)
        numbers.append(sorted_number)
    return numbers

# Define a test function 'test' to demonstrate the 'genNintegersN' function.
def test():
    random_numbers = genNintegersN(6,11,15)
    print(random_numbers)
test()

def printEveryKthInt(N,K):
    for i in range(N+1):
        if (i%K) == 0:
            print(i)

def test():
    printEveryKthInt(12,3) # Print every 3rd integer from 0 to 12
test()

# Define a test function 'test' for plotting random numbers.
def test():
    random_numbers = gen_random(100)# Generate a list of 100 random numbers.
    x_values = []
    for i in range(100):
        x_values.append(i)
    pylab.plot(x_values,random_numbers)
    pylab.title('Random numbers between 0 and 1')
    pylab.xlabel('Sample number')
    pylab.ylabel('Random value')
    pylab.savefig('random_numbers.png')
    pylab.show()
test()

