#Project Name: Minesweeper Genius, by Oscar Yu
#Description: Tells how many mines are adjacent to each of the squares
def program(area):
    lines = int(list[0])
    col = int(list[1])
    list.pop(0) #Gets rid of first two elements (lines/columns)
    list.pop(0)

#Checks to see if correct number of lines/columns
    counter = 0
    for thing in list:
        if thing.isdigit() == True:
            if counter != lines*col:
                print "Error: Number of lines/columns is incorrect!"
                print ""
                exit()
            else:
                break
        counter += 1
    newlist = []
    box = 0 #a is the box number we are working with
    x = 0 #x is just a counter
    string = ""
#Where the magic happens, checks for its location, and then assign a number depending on the location
    try:
        while True:
            if x == col:
                for thing in newlist:
                    string += str(thing)
                print string
                newlist = []
                x = 0
                string = ""
            if list[box] == "*":
                newlist.append('*')
            if box == col*lines:
                break
            if list[box] == ".":
                bombs = 0 #How many adjacent bombs?
                if col == 1:
                    if list[box+1] == "*":
                        bombs += 1
                    if list[box-1] == "*":
                        b+=1
                elif (box+1) % col == 0: #means on right side
                    if 0 <= int(box-1) < col*lines:
                        if list[box-1] == "*":
                            bombs += 1 #Oh look there's a bomb in an adjacent square! Adds 1 to bomb count!
                    if 0 <= int(box+(col-1)) < col*lines:
                        if list[box+(col-1)] == "*":
                            bombs +=1
                    if 0 <= int(box+col) < col*lines:
                        if list[box+col] == "*":
                            bombs += 1
                    if 0 <= int(box-col) < col*lines:
                        if list[box-col] == "*":
                            bombs += 1
                    if 0 <= int(box-(col+1)) < col*lines:
                        if list[box-(col+1)] == "*":
                            bombs +=1
                elif box % col == 0: #mans on left side
                    if 0 <= int(box+1) < col*lines:
                        if list[box+1] == "*":
                            bombs += 1
                    if 0 <= int(box+(col+1)) < col*lines:
                        if list[box+(col+1)] == "*":
                            bombs +=1
                    if 0 <= int(box+col) < col*lines:
                        if list[box+col] == "*":
                            bombs += 1
                    if 0 <= int(box-col) < col*lines:
                        if list[box-col] == "*":
                            bombs += 1
                    if 0 <= int(box-(col-1)) < col*lines:
                        if list[box-(col-1)] == "*":
                            bombs +=1
                else:
                    if 0 <= int(box+1) < col*lines:
                        if list[box+1] == "*":
                            bombs += 1
                    if 0 <= int(box+(col+1)) < col*lines:
                        if list[box+(col+1)] == "*":
                            bombs +=1
                    if 0 <= int(box+col) < col*lines:
                        if list[box+col] == "*":
                            bombs += 1
                    if 0 <= int(box-col) < col*lines:
                        if list[box-col] == "*":
                            bombs += 1
                    if 0 <= int(box-(col-1)) < col*lines:
                        if list[box-(col-1)] == "*":
                            bombs +=1
                    if 0 <= int(box-(col+1)) < col*lines:
                        if list[box-(col+1)] == "*":
                            bombs +=1
                    if 0 <= int(box-1) < col*lines:
                        if list[box-1] == "*":
                            bombs += 1
                    if 0 <= int(box+(col-1)) < col*lines:
                        if list[box+(col-1)] == "*":
                            bombs +=1
                newlist.append(bombs)
            box += 1
            x += 1
    except ValueError:
         print ""

#INTRODUCES THE USER TO THE PROGRAM
print ""
print "                            \033[4m\033[1mWelcome to the Minesweeper Genius\033[0m"
print ""
print "                           Hello, I am the Minesweeper Genius!"
print "             You may tell me where the bombs are in test fields and I will"
print "  represent the fields with the hidden hint numbers. The numbers will tell you how many"
print "                 mines there are adjacent to each of the squares. Have fun!"
print ""
while True:
    try: #Input
        inputFile = open(raw_input("Please insert the file name with the extension: "))
        print ""
        break
    except IOError:
        print ""
        print "  Error: I am confused! This is not a valid file name!"
        print ""
list = []
for line in inputFile:
    for letter in line.strip("\n"):
        list.append(letter)
field = 0 #this count is the Field Number
while True:
    try:
        field +=1
        d = 0
        lines = ""
        col = ""
        while True:
            if list[d].isdigit() == True:
                lines += list[d]
            elif list[d] == " ":
                for i in range(0,d+1):
                    list.pop(0)
                break
            d += 1
        d = 0
        while True:
            if list[d].isdigit() == True:
                col += list[d]
            else:
                for i in range(0,d):
                    list.pop(0)
                break
            d += 1
        list.insert(0,col)
        list.insert(0,lines)
        try:
            lines = int(lines)
            col = int(col)
        except ValueError:
            print "Error: Invalid Input"
            print ""
            exit()
        if not 0 < int(lines) <= 100 or not 0 < int(col) <= 100:
            print "Error: Number of lines or columns have to be between 1 - 100, inclusive!"
            exit()
        print "\033[4m\033[1mField #"+ str(field) + "\033[0m"
        program(0)
        print ""
        for i in range(lines*col):
            list.pop(0)
            if len(list) == 3:
                if list[0] == '0' and list[2] == '0':
                    exit()
    except IndexError:
        print "Error: Invalid Input"
        print ""
        exit()
