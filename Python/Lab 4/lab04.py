import util

def getGrid(n, var): #1 -- Lab 04 -- Print a NxN square of whatever while using nexted loop.
    yAxis = n
    xAxis = n
    r = 0 # value that sets the line
    while r < yAxis: # controls what line it's printing on
        c = 0 # resets the variable to 0 again after every loop
        while c < xAxis: # while loop for actually printing the line
            print var, # var, waits untill the next print statment to dump all prints
            c += 1 # when column hits "n" it will break loop
        print # dumps line of prints
        r += 1 #once this hits the "n" it will stop looping

# I had to use the nots for reference, commented every step to show understanding on what it did. Still confusing as fuck
# and way more difficult compaired to string*number for making blocks.

def triAst(): #2 Lab04 -- Print a triangle using a loop
    n = util.getInt()
    line = 1
    while line <= n:
        print "*"*line
        line += 1
        
def triAst2(n, line): #3 Lab04 -- Print a triangle using recursion
    if line <= n:
        print "*"*line
        line += 1
        return triAst2(n, line)
    
def triAst3():  #4 Lab04 -- Print an upside down triangle
    n = util.getInt()
    line = n
    space = " "
    sd = 0
    while line > 0:
        print space*sd,line*'*'
        sd += 1
        line -= 1

#5 value of e = lim (1+1/h)
def factLoop(var): #Lab03 -- #4 Demon evil factorial loop.
    res = 1
    while var > 1:
        res *= var
        var -= 1
    return res

def vE(n): # n! = n * (n-1) * (n-2) * ... * 1
    var = 1 # Sets the default variable to use throughout the loop
    stop = n # Sets stop to the number sents in through the argument.
             #It's reset to stop because the number will change often
    e = 1   #Sets e to 1, e always starts @ 1
    while var <= stop: # Loops until Var is les then or equal to stop(starting input)
        e = e+(1.0/factLoop(var)) #function to create a new e for printing,
        '''and uses e+1/n!. n! is done by factiorial loop, so the more you want to
loop, the higher the factorial will get, it will start at 1, and go from there
1, 2, 6, 24, 120, 720, 5040, 40320 | Factiorials function as follows: Factorial of
5 for example is 5*4*3*2*1=120
'''
        print "Loop #",var,"\t=\t",e # prints once per loop with 2 variables. 
        var += 1
        
def printMultiples(n, length, col):
    if col <= length:
        print n*col, '\t', 
        col += 1
        return printMultiples(n, length, col)
    else:
        print
    
def printMultTable(i, length):
    if i <= length:
        col = 1
        printMultiples(i, length, col)
        i += 1
        return printMultTable(i, length)