"""
hightemp.py

Simon Lartey
Fall 2023
CS152 Lab 2

This program identifies the maximum temperature and the date it occurred on and outputs the results to the console. It also combines data files using the Python zip function!

"""


# main function
def main():
    
    f1 = open('dates.csv','r')
    f2 = open('temps.csv', 'r')
    f3 = open('blend.csv', 'w')

    for x,y in zip(f1,f2):
        f3.write(x.strip()+","+y.strip()+'\n')
    f3.close()
    
    fp = open( "blend.csv", "r" )
    line = fp.readline()

    hitemp=-200
    hidate=""
   
    for line in fp:
        words = line.split(",")  
        date=words[0]
        temp=float(words[3])
        # print(words)
    
        if temp > hitemp:
            hitemp = temp
            hidate = date
    print(hitemp,hidate)
    print("Highest Temp: %f" % (hitemp))
    print("Highest Temp: %7.3f" % (hitemp))
    print("The highest temperature of %.3f occurred on %s." % (hitemp,hidate))

main()       

    

    # add your code here


# only execute main if this file was executed
# if __name__ == "__main__":
        
