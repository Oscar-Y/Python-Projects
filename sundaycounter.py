#Project Name: Sunday Counter, by Oscar Yu
#Description: Counts number of times Sunday falls on the first of the month between two dates

import datetime #I will be using this to determine the day of the week, as it is efficient.
start = [] #this will be the list containing the values for start date
end = [] #and end date

print ""
print "                             \033[4m\033[1mWelcome to the Sunday Counter\033[0m"
print ""
print "                       Hello! I am sure you have always wondered..."
print "             how many Sundays fall on the first of the month between two dates!"
print "               Well now you can find out with the ULTIMATE SUNDAY COUNTER!!!"
print "  I will tell you how many times Sunday falls on the first of the month between two dates"
print ""

#START YEAR
while True:
    byear = raw_input("\033[1mStart Year\033[0m (e.g. 9, 202, 2014): ")
    try:
        if int(byear) < 1: #Only takes years above 1 obviously
            print ""
            print "   Error: the year cannot be", byear
            print ""
        else:
            start.append(int(byear)) #and then adds year to start list
            break
    except ValueError: #if the input is not a number 
        print ""
        print "   Error: invalid start year. Please follow the format!"
        print ""

#START MONTH
while True:
    bmonth = raw_input("\033[1mStart Month\033[0m (e.g. July, Jul, 07, 7): ")
    if bmonth == "January" or bmonth == "Jan" or bmonth == "1" or bmonth == "01":
        start.append(1)
        break
    elif bmonth == "February" or bmonth == "Feb" or bmonth == "2" or bmonth == "02":
        start.append(2)
        break
    elif bmonth == "March" or bmonth == "Mar" or bmonth == "3" or bmonth == "03":
        start.append(3)
        break
    elif bmonth == "April" or bmonth == "Apr" or bmonth == "4" or bmonth == "04":
        start.append(4)
        break
    elif bmonth == "May" or bmonth == "5" or bmonth == "05":
        start.append(5)
        break
    elif bmonth == "June" or bmonth == "Jun" or bmonth == "06" or bmonth == "6":
        start.append(6)
        break
    elif bmonth == "July" or bmonth == "Jul" or bmonth == "07" or bmonth == "7":
        start.append(7)
        break
    elif bmonth == "August" or bmonth == "Aug" or bmonth == "08" or bmonth == "8":
        start.append(8)
        break
    elif bmonth == "September" or bmonth == "Sep" or bmonth == "09":
        start.append(9)
        break
    elif bmonth == "October" or bmonth == "Oct" or bmonth == "10":
        start.append(10)
        break
    elif bmonth == "November" or bmonth == "Nov" or bmonth == "11":
        start.append(11)
        break
    elif bmonth == "December" or bmonth == "Dec" or bmonth == "12":
        start.append(12)
        break
    else:
        print ""
        print "   This is an invalid start month. Accepted formats: January, Jan, 1, 01"
        print ""

#START DAY
while True:
    bday = raw_input("\033[1mStart Day\033[0m (e.g. 3): ")

#30 days - checks to see day is between 1-30
    try:
        bday = int(bday)
        if start[1] in [4,6,9,11]:
            if 1 <= bday <= 30:
                start.append(int(bday))
                break
            else:
                print ""
                print "   Error: There are only 30 days in your start month!"
                print ""
    except ValueError:
        print ""
        print "   Error: invalid start day. Please follow the format!"
        print ""


#February - checks for leap years and sees if input is valid
    if start[1] == 2: #Thanks to Microsoft Support's steps to determine leap year
        if start[0] % 4 != 0: 
            if 1 <= bday <= 28:
                start.append(int(bday))
                break
            else:
                print ""
                print "   Error: There are only 28 days because", byear, "is not a leap year"
                print ""
        elif start[0] % 4 == 0:
            if start[0] % 100 == 0:
                if start[0] % 400 == 0:
                    if 1 <= bday <= 29:
                        start.append(int(bday))
                        break
                    else:
                        print ""
                        print "   Error: There are only 29 days in February"
                        print ""
                else:
                    if 1 <= bday <= 28:
                        start.append(int(bday))
                        break
                    else:
                        print ""
                        print "   Error: There are only 28 days because", byear, "is not a leap year"
                        print ""
            else:
                if 1 <= bday <= 29:
                    start.append(int(bday))
                    break
                else:
                    print ""
                    print "   Error: There are only 29 days in February"
                    print ""

#31 days - checks to see day is between 1-31
    else:
        if 1 <= bday <= 31:
            start.append(int(bday))
            break
        else:
            print ""
            print "   Error: there can only be max 31 days in a month!"
            print ""

#END YEAR
while True:
    try:
        eyear = raw_input("\033[1mEnd Year\033[0m (e.g. 1, 200, 2014): ")
        if int(eyear) < 1:
            print ""
            print "   Error: the year cannot be", eyear
            print ""
        elif int(eyear) < int(byear):
            print ""
            print "   Error: The end year must be later than the start year!"
            print ""
        elif eyear.isdigit() == True:
            end.append(int(eyear))
            break
    except ValueError: #if the input is not a number 
        print ""
        print "   Error: invalid end year! Accepted formats: 1, 200, 2014"
        print ""

#END MONTH
while True:
    emonth = raw_input("\033[1mEnd Month\033[0m (e.g. July, Jul, 07, 7): ")
    if emonth == "January" or emonth == "Jan" or emonth == "1" or emonth == "01":
        end.append(1)
        break
    elif emonth == "February" or emonth == "Feb" or emonth == "2" or emonth == "02":
        end.append(2)
        break
    elif emonth == "March" or emonth == "Mar" or emonth == "3" or emonth == "03":
        end.append(3)
        break
    elif emonth == "April" or emonth == "Apr" or emonth == "4" or emonth == "04":
        end.append(4)
        break
    elif emonth == "May" or emonth == "5" or emonth == "05":
        end.append(5)
        break
    elif emonth == "June" or emonth == "Jun" or emonth == "06" or emonth == "6":
        end.append(6)
        break
    elif emonth == "July" or emonth == "Jul" or emonth == "07" or emonth == "7":
        end.append(7)
        break
    elif emonth == "August" or emonth == "Aug" or emonth == "08" or emonth == "8":
        end.append(8)
        break
    elif emonth == "September" or emonth == "Sep" or emonth == "09":
        end.append(9)
        break
    elif emonth == "October" or emonth == "Oct" or emonth == "10":
        end.append(10)
        break
    elif emonth == "November" or emonth == "Nov" or emonth == "11":
        end.append(11)
        break
    elif emonth == "December" or emonth == "Dec" or emonth == "12":
        end.append(12)
        break
    else:
        print ""
        print "   Error: invalid end month. Accepted formats: January, Jan, 1, 01"
        print ""

#END DAY
while True:
    eday = raw_input("\033[1mEnd Day\033[0m (e.g. 3): ")
    try:
        eday = int(eday)
        if end[1] in [4,6,9,11]:
            if 1 <= eday <= 30:
                end.append(int(eday))
                break
            else:
                 print ""
                 print "   Error: There are only 30 days in your end month!"
                 print ""
    except ValueError:
        print ""
        print "   Error: invalid end day. Please follow the format!"
        print ""
    if end[1] == 2:
        if end[0] % 4 != 0: 
            if 1 <= eday <= 28:
                end.append(int(eday))
                break
            else:
                print ""
                print "   Error: There are only 28 days because", eyear, "is not a leap year"
                print ""
        elif end[0] % 4 == 0:
            if end[0] % 100 == 0:
                if end[0] % 400 == 0:
                    if 1 <= eday <= 29:
                        end.append(int(eday))
                        break
                    else:
                        print ""
                        print "   Error: There are only 29 days in February"
                        print ""
                else:
                    if 1 <= eday <= 28:
                        end.append(int(eday))
                        break
                    else:
                        print ""
                        print "   Error: There are only 28 days because", eyear, "is not a leap year"
                        print ""
            else:
                if 1 <= eday <= 29:
                    end.append(int(eday))
                    break
                else:
                    print ""
                    print "   Error: There are only 29 days in February"
                    print ""
    else:
        if 1 <= eday <= 31:
            end.append(int(eday))
            break
        else:
            print ""
            print "   Error: There are can only be max 31 days in a month!"
            print ""

#Derived from Python documentation (8.1. datetime). I am appending the weekday integer to the lists
start.append(datetime.datetime(start[0], start[1], start[2], 0, 0, 0, 000000).weekday()) 
end.append(datetime.datetime(end[0], end[1], end[2], 0, 0, 0, 000000).weekday())

sundays = 0 #sunday counter variable

while True:
    if start[2] == 1 and start[3] == 6: #If it's the first of the month and it is a Sunday...
        sundays += 1
    if start == end: #If we reach the end, then we finish!
        print sundays, "Sundays fell on the first of the month between", bmonth, "/", bday, "/", byear, "to", emonth, "/", eday, "/", eyear
        exit()
    else:
        if start[3] == 6: #If it reaches 6 (Sunday), it goes to 0 (Monday)
            start[3] = 0
        else:
            start[3] += 1 #otherwise it just adds 1, such as 4 (Friday) to 5 (Saturday)
        if start[1] == 12 and start[2] == 31: #if it's December 31st, then we add 1 to the year!!!
            start[0] += 1
            start[1] = 1
            start[2] = 1
        elif start[1] == 2: #If it's February (Leap years stuff, similar to earlier)
            if start[0] % 4 != 0:
                if start[2] == 28:
                    start[2] = 1
                    start[1] = 3
                else:
                    start[2] += 1
            elif start[0] %4 == 0:
                if start[0] % 100 == 0:
                    if start[0] % 400 == 0:
                        if start[2] == 29:
                            start[2] = 1
                            start[1] = 3
                        else:
                            start[2] += 1
                    else:
                        if start[2] == 28:
                            start[2] = 1
                            start[1] = 3
                        else:
                            start[2] += 1
                else:
                    if start[2] == 29:
                        start[2] = 1
                        start[1] = 3
                    else:
                        start[2] += 1
        elif start[1] in [4,6,9,11]: #If month has 30 days
            if start[2] == 30:
                start[2] = 1
                start[1] += 1
            else:
                start[2] += 1
        else: #If month has 31 days...
            if start[2] == 31:
                start[2] = 1
                start[1] += 1
            else:
                start[2] += 1
