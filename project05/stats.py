'''
Simon Lartey,
09/28/2023,
CS 152B
the program computes different types of statistics of a list of data
'''
#computes the sum of the list of data
def sum_numbers(numbers):
    sum_numbers = 0.0
    for  items in numbers:
        sum_numbers +=items
    return sum_numbers


# computes the sum of the list of data 
def mean(data):
    total = sum_numbers(data)
    mean = total / len(data)
    return mean
#computes the minimum value in the list of data
def minimum(data):
    minimum_value = 10000
    for item in data:
        if item < minimum_value:
            minimum_value = item
    return minimum_value
    
#computes the maximum data in the list of data
def maximum_data(data):
    maximum_value = -1
    for item in data:
        if item > maximum_value:
            maximum_value = item
    return maximum_value

#computes the index at which the minimum value in the occur
def minimum_value_index(data):
    minimum_value = 1000
    minimum_value_index = -1
    for i, item in enumerate(data):
        if item < minimum_value:
            minimum_value = item
            minimum_value_index = i
    return minimum_value_index

 #computes the index at which the maximun value in the data occurs   
def maximum_value_index(data):
    maximum_value = -1
    
    for i, item in enumerate(data):
        if item > maximum_value:
            maximum_value = item
            maximum_value_index = i
    return maximum_value_index

#finding the variance from the mean 
def variance(nums):
	##Compute the mean of nums
    total = sum_numbers(nums)
    mean = total / len(nums)
    

	#Make a new empty list: squared_nums_minus_means
    squared_nums_minus_means = []
	#Loop over the values in nums
    for item in nums:
#For each value, append the square of ( the value minus the mean of nums ) to squared_nums_minus_means
        squared_diff_value =(item - mean)**2
        squared_nums_minus_means.append(squared_diff_value)

#You can take the square of an expression as (expression)**2
	#Compute the sum of squared_nums_minus_means and divide it by the size of nums minus 1
        var = sum(squared_nums_minus_means)/ (len(nums)-1)
	#Return the value you just computed
    return var
def test():
    my_list = [1, 2, 3, 4]
    
    print("sum of numbers:",sum_numbers(my_list))
    print("Mean:", mean(my_list))
    print("Min:", min(my_list))
    print("Max:", max(my_list))
    print("Index of Min:", minimum_value_index(my_list))
    print("Index of Max:", maximum_value_index(my_list))
    print("variance:", variance(my_list))

if __name__ == "__main__":
   test()
   