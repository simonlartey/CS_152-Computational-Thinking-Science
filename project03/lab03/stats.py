'''
Simon Lartey,
09/28/2023,
CS 152B
'''
#sum numbers in a list
def sum_numbers(numbers):
    sum_numbers = 0.0
    for  items in numbers:
        sum_numbers +=items
    return sum_numbers

def test():
    my_list = [1, 2, 3, 4]
    result = sum_numbers(my_list)
    print(result)
if __name__ == "__main__":
    test()

