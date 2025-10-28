'''
Simon Lartey,
09/28/2023,
CS 152B
this program computes differnt types of statistics of a list of data'''

#ompute the median of a list of data
def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        first_middle = sorted_data[n // 2]
        second_middle = sorted_data[n // 2 - 1]
        median_value = (first_middle + second_middle) / 2
    else:
        median_value = sorted_data[n // 2]
    return median_value

#finding the range of data
def data_range(data):
    return max(data) - min(data)

#finding the interquatile range 
def interquartile_range(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        lower_half = sorted_data[:n // 2]
        upper_half = sorted_data[n // 2:]
    else:
        lower_half = sorted_data[:n // 2]
        upper_half = sorted_data[n // 2 + 1:]
    lower_quartile = median(lower_half)
    upper_quartile= median(upper_half)
    return upper_quartile - lower_quartile

import math

#find the sum of numbers in the data set
def sum_numbers(numbers):
    sum_numbers = 0.0
    for  items in numbers:
        sum_numbers +=items
    return sum_numbers

#compute the variance
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


	#Compute the sum of squared_nums_minus_means and divide it by the size of nums minus 1
        var = sum(squared_nums_minus_means)/ (len(nums)-1)
    return var

#finding the standard deviation from the variance 
def standard_deviation(data):
    var = variance(data)
    standard_deviation = math.sqrt(var)
    return standard_deviation

if __name__ == "__main__":
    my_list = [11, 22, 13, 41, 23, 34, 45, 32, 12, 14 , 15, 16, 17, 18, 41, 21, 78, 99, 98 ]
    #print data
    print("Median:", median(my_list))
    print("Range:", data_range(my_list))
    print("Interquatile range:", interquartile_range(my_list))
    print("Standard Deviation:", standard_deviation(my_list))
