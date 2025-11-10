'''CS 152B
Simon Lartey
11/02/2023
projec06
'''
import random
import math

# Perform binary search to find the target element in a sorted list.
def searchSortedList(my_list, target):
    my_list.sort()
    start_idx = 0
    end_idx = len(my_list)-1
    iterations = 0
    target_index = -1 

# Binary search loop to find the target element within the sorted list
    while start_idx < end_idx:
        iterations += 1  # Increment the iteration count
        mid = math.floor((start_idx + end_idx)/2)# Calculate the midpoint.
        if my_list[mid] == target:   
           target_index = mid
           break
        elif my_list[mid] < target:
            start_idx = mid
        else:
            end_idx = mid
       

    return target_index, iterations

#testing
my_list = [5,6,7,8,9,10]
results = searchSortedList(my_list,9) # Search for '9' in the list.
second_results = searchSortedList(my_list, 4) # Search for '4' in the list.
print(results)
print(second_results)

# Generate a sorted list of N unique integers with one occurrence of 42.
def sorted_list(N):
    num_list = [random.randint(1, N) for i in range(N - 1)]  # Generate N-1 random integers
    
    # Insert the value 42 at a random index in the list.
    insert_idx = random.randint(0, N - 1)
    num_list.insert(insert_idx, 42)  # Insert 42 at a random index

  # Return the list sorted in ascending order.   
    return sorted(num_list)


def test(N):
    num_list = sorted_list(N)
    target_index, tries = searchSortedList(num_list, 42)
    return target_index,tries

if __name__ == "__main__":
    N_values = [1000, 10000, 100000, 1000000]
   # Print a header for the output table. 
    print("List size\tNumber of steps\tLog base 2 of list size\tTarget Index")
        # Loop through different list sizes, perform tests, and print the results.
    for N in N_values:
        target_index,tries = test(N)
         # Calculate the base-2 logarithm of N for comparison
        log2_N = math.log2(N)
       
        # Print the results in a tabular format.
        print(f"{N}\t\t{tries}\t\t{log2_N}\t{target_index}")

