#Project Name: Permutation Searcher
#Description: Finds out permutations, given the series of numbers and the placement of it in a list of all possible permutations numerically

from itertools import permutations

print ""
print "                             \033[4m\033[1mWelcome to the Permutation Searcher\033[0m"
print ""
print "                       Hello! I am sure you have have been trying to find"
print "                     your dream lexicographic permutation for some time now..."
print "    Well now you can find out your dream lexicographic permutation with the Permutation Searcher"
print "      With a series of digits and your permutation placement, I will tell you your permutation!"
print ""
while True:
    while True:
        number = raw_input("Please give me a series of digits or letters: ")
        number = "".join(sorted(str(number))) #Thanks to hughdbrown from stackoverflow on how to rearrange digits in order
        break
    while True:
        place = raw_input("Which place is this permutation in a list of all possible permutations listed numerically?: ")
        if place.isdigit() == False:
            print ""
            print "   Error: placement number must be a number!"
            print ""
        elif int(place) < 1:
            print ""
            print "   Error: placement number must be greater than 0!"
            print ""
        else:
            list = []
            for thing in permutations(number):
                if thing not in list:
                    list.append(thing)
                answer = ""
            try:
                for thing in list[(int(place))-1]: #To join all the strings to get the answer
                    answer += thing
                print ""
                print "   Permutation #" + place + " for " + number + " is \033[4m\033[1m" + answer + "\033[0m"
                print ""
                break
            except IndexError:
                print ""
                print "   Error: there are not", place, "possible permutations for", number
                print ""
    while True:
        again = raw_input("Do you want to play again? (Y/N): ")
        if again == "Y" or again == "y" or again == "yes" or again =="Yes":
            break
        elif again == "N" or again == "n" or again == "No" or again == "no":
            print ""
            print "   Thanks for playing. Bye!"
            print ""
            exit()
        else:
            print ""
            print "   Error: only use 'Y' or 'N' (without apostrophes)"
            print ""
