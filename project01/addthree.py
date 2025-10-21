'''Simon Lartey
09/15/2023
CS152B
lab01
this program prints the average and sum of three numbers'''
print('version 1')
print('sum', 42+21+5)
print('average',(42+21+5)/3)

print('version 2')
print('sum', 42+21+5)
print('average',(42+21+5//3))

print('version 3')
print('sum', 42+21+5.0)
print('avg',(42+21+5)//3.0)

print('version 4')
a=42
b=21
c=5
print('sum', a+b+c)
print('avg',(a+b+c)/3.0)

print('version 5')
SO=99
IO=1
RO=0
print('population size',SO+IO+RO)

print('version 6')
SO=99
IO=1
RO=0
def compute_population_size(SO,IO,RO):
    print('population size',SO+IO+RO)
compute_population_size(SO,IO,RO)
compute_population_size(20,20,10)
compute_population_size(8,16,1)

print('version 7')
SO=int(input("Enter the SO for the similation: "))
IO=int(input("Enter the IO for the simulation: "))
RO=int(input("Enter the RO for the simulation: "))

def compute_population_size(SO,IO,RO):
    print('population size',SO+IO+RO)
compute_population_size(SO,IO,RO)

print('version 8')

def compute_population_size(SO,IO,RO):
    return('population size',SO+IO+RO)
SO=int(input("Enter the SO for the similation: "))
IO=int(input("Enter the IO for the simulation: "))
RO=int(input("Enter the RO for the simulation: "))

population_size=compute_population_size(SO,IO,RO)
print( "Population size:", population_size )


