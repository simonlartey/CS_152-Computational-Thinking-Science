'''
Simon Lartey,
09/28/2023,
CS 152B
'''

numbers = [5, 3, 6, 1, 2]
#access the first element of a list
first_number = numbers[0]
#access the fourth element of a list
fourth_number = numbers[3]
print( first_number )
print(fourth_number)

# add items to the end of a list,
numbers.append(7)
print( numbers )

#updating a list
numbers[0] = 4
numbers[2] = 9
numbers[4] = 8
print(numbers)
