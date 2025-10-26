"""
july_split.py

Simon Lartey
Fall 2023
CS152 project 2

This program extract data differnt files into separate files

"""

def main():
    with open('Goldie2019.csv','r') as file:
        fp = open('Goldie2019July.csv','w')
        headerline = file.readline()
        fp.write(headerline)
        for line in file:
            if  line.startswith('07/'):
                fp.write(line)   
    
    with open('MLRCWeather2019.csv','r') as file:
        fp = open('MLRC2019July.csv','w')
        headerline = file.readline()
        fp.write(headerline)
        for line in file:
            if  line.startswith('07/'):
                fp.write(line)   
            
    with open('Goldie2019July.csv', "r") as file:
        file_1 = open("Goldie2019JulyFiltered.csv",'w')
        for line in file:
            words = line.split(",")
            date = words[0]
            temp_3m = words[11]
            temp_5m = words[16]
            temp_7m = words[17]
            surface_par = words[21]
            selected_line = date + "," + temp_3m + "," + temp_5m + "," + temp_7m + "," + surface_par + "\n"
            file_1.write(selected_line)

    with open('MLRC2019July.csv', "r") as file:
        file_2 = open("MLRC2019JulyFiltered.csv",'w')
        for line in file:
            words = line.split(",")
            air_temp = words[2]
            wind_speed = words[5]
            wind_direction = words[7]
            selected_line =  air_temp + "," + wind_speed + "," + wind_direction + "\n"
            file_2.write(selected_line)

    Goldie_july_filtered = open("Goldie2019JulyFiltered.csv", "r")
    MLRC_july_filtered = open("MLRC2019JulyFiltered.csv", "r")
    with open("GoldieMLRCJuly.csv" , "w") as output:
        for line_Goldie, line_MLRC in zip(Goldie_july_filtered, MLRC_july_filtered):
            output.write(line_Goldie.strip()+ "," +line_MLRC)

if __name__ == "__main__":
    main()