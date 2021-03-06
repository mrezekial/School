import util
import lab04

def restart(): #Made for restarting the program.
    answer = raw_input("Do you want to restart this program? ")
    if answer.strip() in "y Y yes Yes YES".split():
        print " "
        return start()
    else:
        print '\n\nThank you for using my program.\n\nKeegan Bailey\nC0369801'

def selected_option(n):
    if n == 1:
        print "Print a NxN square of whatever while using nexted loop."
        n = util.getInt()
        var = raw_input('Please input a variable: ')
        lab04.getGrid(n, var)
        return restart()
    if n == 2: 
        print "Print a triangle of '*'s"
        lab04.triAst()
        return restart()
    if n == 3:
        print "Print a triangle of '*'s"
        n = util.getInt()
        line = 1
        lab04.triAst2(n, line)
        return restart()
    if n == 4:
        print "Print a triangle of '*'s upside down"
        lab04.triAst3()
        return restart()
    if n == 5:
        print "Prompt for the number of terms to use and then calculate the value of e"
        n = util.getInt()
        lab04.vE(n)
        return restart()
    if n == 6:
        length = util.getInt('input a number for the multTable length: ', 'YOU DUN GOOFd')
        i = 1
        lab04.printMultTable(i, length)
        return restart()

#Idiot checking to see if they entered an invalid option.

def idiot_check(n):
    if n > 8:
        print '\nYou did not input a valid number, please try again.\n\n\n'
        return restart()
    elif n < 1:
        print '\nYou did not input a valid number, please try again.\n\n\n'
        return restart()
    elif 8 > n > 0:
        print '\nYour input was accepted.\n'
        return selected_option(n)
    else:
        print '\nError #0\n'
        return restart()
    
def start():  # start of the program.
    print "Please select one of the following options:\n"
    print "#1 --  Print a NxN square of whatever while using nexted loop."
    print "#2 --  Triangle of asterisks. (loop)"
    print "#3 --  Triangle of asterisks. (rec)"
    print "#4 --  Triangle of asterisks. (upside down)"
    print "#5 --  Calculate the value of e"
    print "#BONUS -- Print multTable using recursion"
    print "--------------------------------------------------------------"
    n = input('Please select an option now: ') 
    return idiot_check(n) # checks to see if the user is retarded.

if __name__ == '__main__':
    print "Keegan Bailey\nC0369801\nComp112 -- Lab04\n\n"
    start()
