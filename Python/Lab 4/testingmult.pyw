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
    
length = input('put a number in here: ')
i = 1
printMultTable(i, length)