'''
Simon Lartey,
09/28/2023,
CS 152B
this program computes differnt types of statistics of a list of data '''
import sys
import stats
def main( filename, column_id):
# assign to fp the result of opening the file hurricanes.csv for reading
    fp = open(filename,"r")


# assign to line the first line of the data file
    line = fp.readline()
# assign to headers the result of splitting the line using commas
    headers = line.split(",")
# print headers
    print(headers)
# assign to a list variable named data an empty list
    data = []
# for all of the remaining lines in the file
  # assign to items t he result of splitting the line using commas
    for line in fp:
        items = line.split(",")
    # append the second item cast as a float to data (which index?
        data.append(float(items[column_id]))
# close the data file
    fp.close
# print data
    print(data)
    sum_of_values_in_data = stats.sum_numbers(data)
    print("Sum of values: ", sum_of_values_in_data)
    mean_of_values_in_data = stats.mean(data)
    print("mean of values: ",mean_of_values_in_data)
    variance_of_data = stats.variance(data)
    print("variance of data: ",variance_of_data)
    maximum_value = stats.maximum_data(data)
    print("maximum value: ", maximum_value)
    minimum_value = stats.minimum(data)
    print("minimum value: ", minimum_value)
    minimum_value_index = stats.minimum_value_index(data)
    print("minimum value index: ", minimum_value_index)
    maximum_value_index = stats.maximum_value_index(data)
    print("maximum value index: ",maximum_value_index)
if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
