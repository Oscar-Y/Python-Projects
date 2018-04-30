#BELOW program(n) simply takes a number, finds how many letters are in it, and returns it:
def program(n):
    ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8] #len of numbers to  19. index 0 is 0 to make indexes match up with their number
    tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6] #1 = ten, 2 = twenty...
    num = [] #this list will be the number split into its digits (e.g. 123 = [1, 2, 3]
    ans = 0 #how many letters are used to write n, n being each number.
    for thing in n: #to split the number and make list
        num.append(int(thing))
    if int(n) < 20: #1-20
        ans += ones[int(n)]
    if 20 <= int(n) <= 99: #20-99
        ans += tens[num[0]]
        ans += ones[num[1]]
    if len(n) == 3: #100-999
        ans += ones[num[0]] + len("hundred")
        if num[1] != 0 or num[2] != 0: #and is not used for multiples of 100 (100, 200, 300...)
            ans += len("and")
        if int(str(num[1]) + str(num[2])) < 20: #hundred and... 1-20
            ans += ones[int(str(num[1]) + str(num[2]))]
        else:
            ans += tens[num[1]] + ones[num[2]]
    if len(n) == 4: #1000-9999
        ans += ones[num[0]] + len("thousand")
        if num[1] != 0 or num[2] != 0 or num[3] != 0: #and is not used for multiples of 1000 (1000, 2000, 3000...)
            ans += len("and")
        if int(str(num[2]) + str(num[3])) < 20: #for 1-20
            ans += ones[int(str(num[2]) + str(num[3]))]
        else:
            ans += tens[num[2]] + ones[num[3]] #for 21-99
        if num[1] != 0: #if one thousand and... hundred
            ans += ones[num[1]] + len("hundred")
    return ans



#BELOW: This is an introduction, telling the user what the program does.
print ""
print "                \033[4m\033[1mWelcome to Number Letter Counts!\033[0m"
print ""
print "  This program will find the total number of letters used if all"
print "   the numbers from one to a maximum number is written in words."
print "Note: Our program only works from numbers 1-9999. I will update it"
print " to allow more numbers in the future if there is a lot of support." 
print ""



#BELOW: Deals with user input behaviour. User-friendly interface.
while True:
    while True:
        number = raw_input("     Please enter a natural number for the maximum: ") #natural numbers are integers above 1. (1, 2, 3, 4, 5, 6...)
        try:
            int(number) #checks to see if the number is an integer
        except ValueError:
            print "      Error:", number, "is not a natural number"
            continue
        if 1 <= int(number) <= 9999: #checks to see if number between 1-9999
                break
        else:
            print "      Error:", number, "is not from 1-9999"
    numbersnum = []
    for numbers in range(1, int(number) + 1):
        numbersnum.append(numbers)
    final = 0
    for thing in numbersnum:
        final += program(str(thing))
    print ""
    print "\033[4m\033[1m" + str(final) + "\033[0m", "letters would be used to write all the numbers 1 to", number, "in words."
    print ""
    while True:
        playagain = raw_input("Would you like to play again? (Y or N): ")
        if playagain == "N":
            print "Thanks for playing! Good bye!"
            print ""
            exit()
        elif playagain == "Y":
            break
        else:
            print " Error: Please type 'Y' or 'N' (without apostrophes)."
