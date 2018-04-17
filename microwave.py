#Project Name: THE MICROWAVE by Oscar Yu
#Description: Takes the microwave cooking countdown and the clock time and outputs whether the microwave ever displays the correct time.

#Notes: 5*x and x += 1 is used to refer to each test case. x is one less than the case #.
#    This algorithm simply puts all the numbers into a list and works with each number.
#    This technique is similar to another problem: Number Letter Counts
#    If the user had an invalid input, I did not work with it. For example, if T is 2 - two test cases - but there are 3 test cases, I made sure the user knew they made a mistake, instead of continuing to test their cases."

#---- START ----

def test(x):
    while True:
        if not 0 <= int(times[5*x+1]) <= 23 or not 0 <= int(times[5*x+2]) <= 59 or not 0 <= int(times[5*x+3]) <= 59: #Checks requirements of clock time
            print "Case " + str(x + 1) + ": \033[4m\033[1mERROR\033[0m"
            print "   Error: THE MICROWAVE is confused - invalid clock time! Aborting..."
            print ""
            exit()
        if not 0 <= int(times[5*x+4]) <= 23: #Makes sure minutes range from 00 to 23
            print "Case " + str(x + 1) + ": \033[4m\033[1mERROR\033[0m"
            print "   Error: THE MICROWAVE catches on fire - maximum cooking time is 23m and 59s. Aborting..."
            print ""
            exit()
        if not 0 <= int(times[5*x+5]) <= 59: #Makes sure seconds range from 00 to 59
            print "Case " + str(x + 1) + ": \033[4m\033[1mERROR\033[0m"
            print "   Error: THE MICROWAVE is confused - invalid cooking time. Aborting..."
            print ""
            exit()
#Clock
        if times[5*x+3] == '59': #when seconds are 59
            if times[5*x+2] == '59':
                if times[5*x+1] == '23': #when 23:59:59 - goes to 00:00:00 next
                    times[5*x+1] = times[5*x+2] = times[5*x+3] = '00'
                else: #hours tick
                    times[5*x+1] = str(int(times[5*x+1]) + 1)
                    times[5*x+2] = times[5*x+3] = '00'
            else: #minutes tick
                times[5*x+2] = str(int(times[5*x+2]) + 1)
                times[5*x+3] = '00'
        else: #seconds tick
            times[5*x+3] = str(int(times[5*x+3]) + 1)
#Cooking
        if int(times[5*x+5]) == 0:
           if int(times[5*x+4]) == 0: #checks for NO
                print "Case " + str(x + 1) + ": \033[4m\033[1mNO\033[0m"
                print "   Clock:", "%02d" % (int(times[5*x+1])) + ":" + "%02d" % (int(times[5*x+2])), " Cooking Time: END"
                print ""
                break
           else: #minutes tick
                times[5*x+4] = str(int(times[5*x+4]) - 1)
                times[5*x+5] = '59'
        else: #seconds tick
            times[5*x+5] = str(int(times[5*x+5]) - 1)
#Checks for YES 
        if int(times[5*x+1]) == int(times[5*x+4]) and int(times[5*x+2]) == int(times[5*x+5]):
            print "Case " + str(x + 1) + ": \033[4m\033[1mYES\033[0m"
            print "   Clock:", "%02d" % (int(times[5*x+1])) + ":" + "%02d" % (int(times[5*x+2])), " Cooking Time:", "%02d" % (int(times[5*x+4])) + ":" + "%02d" % (int(times[5*x+5]))
            print ""
            break

#INTRODUCES THE PROGRAM TO THE USER IN AN APPEALING WAY
print ""
print "                            \033[4m\033[1mWelcome to THE MICROWAVE\033[0m"
print ""
print "                           Hello, I am THE MICROWAVE!"
print "        I can tell you the clock time and the time left that I will cook for."
print "  When I count down the remaining time left, I might also display the correct time!"
print "Using the test cases you provide, I will tell you if the times match! Have fun cooking!"
print ""

#ASKS THE USER FOR A FILE
while True:
    try: #Input
        inputFile = open(raw_input("Please insert the file name with the extension: "))
        print ""
        break
    except IOError:
        print ""
        print "  Error: I am confused! This is not a valid file name!"
        print ""

#CREATES A LIST USING THE FILE
times = []
for line in inputFile:
    for word in line.replace(':',' ').replace('\n','').replace('\r','').split(' '):
        times.append(word)

#CHECKS NUMBER OF TEST CASES
T = times[0]
if T.isdigit() == True: #Checks to see if test cases is a number
    if int(T)*5+1 != len(times): #Checks to see if test cases # is accurate
        print "  THE MICROWAVE explodes: Check the number of test cases or look for bad formatting!"
        print ""
        exit()
else:
    print "   Error: I am confused! The number of test cases must be a whole number!"
    print ""
    exit()

#CHECKS TIMES
for thing in times:
    if thing.isdigit() == False:
        print "   THE MICROWAVE explodes: Invalid input! (check to see that you only used numbers)"
        print ""
        exit()

#CHECKS TO SEE IF ALL TEST CASES ARE DONE
case = -1 #starts at -1 for the case to be 0 at the start of the while loop
while True:
    case += 1
    if case == int(T): #If all the test cases are done, thank the user!
        print "Thank you for cooking your food with THE MICROWAVE!"
        print "             Hope to see you soon!"
        print ""
        exit()
    else: #and if all test cases are not done, work on the next test case
        test(case)
