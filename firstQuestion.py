#!/usr/bin/python
##Weiqi Huang
'''Description
   Given a list of people with their birth and end years (all between 1900 and 2000), find the year with the most number of people alive.
'''
def main():
    ##create the empty list to store the year of those people.
    year = []
    name = []
    wholeName= ""
    ##open the txt file
    with open ('Name.txt','r') as f:
        ##Read each line in the file
        for line in f.readlines():
            ##append the year to my list
            year.append(line[-5:-1])
            name.append(line)
    ##sort the year and see the repeat times.
    year.sort()
    count = 1
    year1 = ""
    ##check which one is the most year they alive
    for item in year:
        if year.count(item) > count :
            count = year.count(item)
            year1 = item
    ##print the whole name of them
    for items in name:
        if year1 == items[-5:-1]:
            wholeName = wholeName + items +"\n"
    print "There are",count,"people who were born in",year1,"\n"
    print "The people are list below :\n",wholeName
    outPut = open('Output.txt','w')
    outPut.write("There are"+" "+str(count)+" "+"people who were born in"+" "+year1+"\n")
    outPut.write("The people are list below :\n"+wholeName)
main()
