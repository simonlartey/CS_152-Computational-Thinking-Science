"""
extract.py

Simon Lartey
Fall 2023
CS152 project 2

this program extracts data from "GoldieMLRCJuly.csv" to 'Goldie2019July3PMAirTemp.csv'

"""
def main():
    fp = open("GoldieMLRCJuly.csv" , "r")

    # Open the file "Goldie2019July3PMAirTemp.csv" in write mode and assign it to 'file'.
    with open('Goldie2019July3PMAirTemp.csv', 'w') as file: 
        lines = fp.readlines()
        file.write("Day, 3pMtemp\n")
        day = 1

        # Iterate through each line in the 'lines' list, starting from the second line (index 1)
        for line in lines[1:]: 
            words = line.split(",")
            if "3:03:00 PM" in words[0]:

                # Write the day and the 3:03 PM temperature to the 'file'.
                file.write(str(day) + ", " + words[5]+'\n')

                # Increment the 'day' counter for the next iteration.
                day+=1
    fp.close()
if __name__ == "__main__":
	main()


