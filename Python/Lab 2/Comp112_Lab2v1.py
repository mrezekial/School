#Comp 112 Lab 2 - Keegan Bailey 11/10/2012 (Python 2.7.3)
import time
import math

def restart(): #Made for restarting the program.
    answer = raw_input("Do you want to restart this program? ")
    if answer.strip() in "y Y yes Yes YES".split():
        return start()
    else:
        print 'kthxbye'

# ------------------------------------------------------------------------------

def c2f(n): #Celsius to Fahrenhiet
    print n*(9.0/5)+32,'degrees Fahrenheit!'
    raw_input('Press enter to continue...')
    return restart()

def f2c(n): #Farenhiet to Celsius
    x =(n-32)*(5/9.0)
    print round(x,2),'degrees Celcius!'
    raw_input('Press enter to continue...')
    return restart()

def AofSq(n): #Area of a quare
    n = n**2
    print 'The area of the rectangle is',float(n),'squared!'
    raw_input('Press enter to continue...')
    return restart()
    
def AofRec(L, W):
    A = L*W
    print 'The area of the rectangle is',float(A),'squared!'
    raw_input('Press enter to continue...')
    return restart()

def AofRTriangle(B, H):
    A = (B*H)/2
    print 'The area of the right triangle is',float(A),'squared!'
    raw_input('Press enter to continue...')
    return restart()
    
def HypOfRTriangle(B, H):
    c = math.sqrt(B**2+H**2)
    print '|\\\n| \\<--- Hypotenuse!\n|  \\\n|___\\\nThe hypotenuse of the right triangle is',("%.3f"%c),'squared!'
    raw_input('Press enter to continue...')
    return restart()

def CircOfCircle(n):
    n = 2*pi*n
    print 'The hypotenuse of the circumference of a circle',round(c,3),'!'
    raw_input('Press enter to continue...')
    return restart()

def AreaOfCircle(n):
    n = pi*n**2
    print 'The area of the circle is',round(c,3),'!'
    raw_input('Press enter to continue...')
    return restart()

def FractionToDecimal(N, D):
    N = float(N)
    D = float(D)
    X = N/D
    print 'The decimal is',X,'!'
    raw_input('Press enter to continue...')
    return restart()

def Average(n1, n2, n3):
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    x = (n1+n2+n3)/3
    print 'The average is',round(x,3),'!'
    raw_input('Press enter to continue...')
    return restart()

def SumProductRemainder(n1, n2):
    n1 = float(n1)
    n2 = float(n2)
    x = (n1+n2)
    x2 = (n1*n2)
    x3 = (n1 % n2)
    print 'Here are the results!\n\nSum: ',x,'\nProduct: ',x2,'\nRemainder of the 2 numbers devided is: ',x3
    raw_input('Press enter to continue...')
    return restart()

def Journey(km, km2, L, L2):
    km = float(km)
    km2 = float(km2)
    km3 = km2-km
    L = float(L)
    L2 = float(L2)
    L3 = L-L2
    L3 = float(L3)
    d = L3/km3
    d = float(d)
    print 'Here are the results!\n\nYou consumed',L3,'litres of gas!\nYour average consumption was',round(d,3),'litres per Km!'
    raw_input('Press enter to continue...')
    return restart()

def CND2USD(n):
    USD = 1.0181
    money = n*USD
    print '\nHere are the results!\n\nYou have $',money,'USD'
    raw_input('Press enter to continue...')
    return restart()
    
def BMI(H, W):
    BMI = W/(H*H)
    print 'Here are the results!\n\nYou have a BMI of: ',BMI
    raw_input('Press enter to continue...')
    return restart()

def HullSpeed(n):
    L = float(L)
    K = 1.35*(L**0.5)
    print '\nHere are the results!\n\nYou have a hull speed of: ',round(K,3)
    raw_input('Press enter to continue...')
    return restart()

def GasBill(first, final, gas, days):
    first = float(first)
    final = float(final)
    gas = final-first
    dcost = days*9.02/100
    gcost = gas*1.433/100
    hcost = ((days*9.02)+(gas*1.433))*0.12
    bill = ((days*9.02)+(gas*1.433))*1.12
    print 'Here are the results!\n\n  Day Cost: $',round(dcost,2),'\n  Gas Cost: $',round(gcost,2),'\n  HST 12%: $',round(hcost,2),'\n ------------------ \n  Total Cost: $',round(bill,2)," "
    raw_input('Press enter to continue...')
    return restart()
  
def Morgage():
    rate = float(rate)
    R = (rate/12)/100
    T = years*12
    A = (P*R*(R+1)**T)/((R+1)**T-1)
    print '\nHere are the results!\n\nLoan Ammount: $',P,'\nIntrest Rate: %',R
    raw_input('Press enter to continue...')    
    return restart()
# ------------------------------------------------------------------------------

def selected_option(n): # Lab 2 questions are in this def
    if n == 1:
        print 'Converting Celsius to Fahrenheit.'
        raw_input('Press enter to continue...')
        n = input('Please insert Celsius temperature: ')
        return c2f(n)
    elif n == 2:
        print 'Converting Fahrenheit to Celcius.'
        raw_input('Press enter to continue...')
        n = input('Please insert Fahrenheit temperature: ')
        return f2c(n)
    elif n == 3:
        print 'Calculating area of a square.'
        raw_input('Press enter to continue...')
        n = input('Please insert the side\'s length: ')
        return AofSq(n)
    elif n == 4:
        print 'Calculating area of a rectangle.'
        raw_input('Press enter to continue...')
        L = input('Please insert the length: ')
        W = input('Please insert the width: ')
        return AofRec(L, W)
    elif n == 5:
        print 'This program will give you the area of a right triangle.'
        raw_input('Press enter to continue...')
        print "\n|\\\n| \\\n|  \\\n|___\\\n<---> = Base"
        B = input('Please insert the base: ')
        print "|\\    ^\n| \\   |\n|  \\  | = Height\n|___\\ |"
        H = input('Please insert the height: ')
        return AorRTriangle(B, H)
    elif n == 6:
        print 'This program will give you the hypotenuse of a right triangle.'
        raw_input('Press enter to continue...')
        print "\n|\\\n| \\\n|  \\\n|___\\\n<---> = Base"
        B = input('Please insert the base: ')
        print "|\\    ^\n| \\   |\n|  \\  | = Height\n|___\\ |"
        H = input('Please insert the height: ')
        return HypOfRTriangle(B, H)
    elif n == 7:
        pi = math.pi
        print 'This program will give you the circumference of a circle.'
        raw_input('Press enter to continue...')
        n = input('Please insert the radius: ')
        return CircOfCircle(n)
    elif n == 8:
        pi = math.pi
        print 'This program will give you the area of a circle.'
        raw_input('Press any key to continue...')
        n = input('Please insert the radius: ')
        return AreaOfCircle(n)
    elif n == 9:
        print 'This program will convert a fraction to a decimal.'
        raw_input('Press enter to continue...')
        N = input('Please insert the numerator (top number): ')
        D = input('Please insert the denominator (bottom number): ')
        return FractionToDecimal(N, D)
    elif n == 10:
        print 'This program will give you the average of 3 numbers.'
        raw_input('Press enter to continue...')
        n1 = input('Please insert the 1st number: ')
        n2 = input('Please insert the 2nd number: ')
        n3 = input('Please insert the 3rd number: ')
        return Average(n1, n2, n3)
    elif n == 11:
        print 'This program will calculate two numbers. It will give you sum, product, and the remainder of the first divided by the second.'
        raw_input('Press enter to continue...')
        n1 = input('Please insert the 1st number: ')
        n2 = input('Please insert the 2nd number: ')
        return SumProductRemainder(n1, n2)
    elif n ==12:
        print 'This program will calculate how much fuel you consumed, and your average consumption on your journey.'
        raw_input('Press enter to continue...')
        km = input('Please insert your kilometers at the START of the journey: ')
        km2 = input('Please insert your kilometers at the END of your journey: ')
        L = input('Please insert how many litres of gas you had at the START of your journey: ')
        L2 = input('Please insert how many litres of gas you had at the END of your journey: ')
        return Journey(km, km2, L, L2)
    elif n == 13:
        print 'This program will convert Canadian curency to US at the current exchange rate.\n(1 Canadian dollar = 1.0181 US dollars) <- LOL USA'
        raw_input('Press enter to continue...')
        n = input('Please insert how many Canadian currency you have: ')
        return CND2USD(n)
    elif n == 14:
        print 'This program will calculate your BMI based off your weight and height in METRIC.'
        raw_input('Press any key to continue...')
        H = input('Please insert how tall (in METRES) you are: ') #example 1.83m
        W = input('Please insert how fat (in KILOGRAMS) you are: ') #example 95.5kg
        return BMI(H, W)
    elif n == 15:
        print 'This program will calculate the hull speed (in knots) of your boat based off the length.'
        raw_input('Press any key to continue...')
        n = input('Please insert how length of your boat (in FEET): ') #example 120
        return HullSpeed(n)
    elif n == 16:
        print 'This program will calculate and print a bill based off meter reading against days (I think).'
        raw_input('Press any key to continue...')
        first = input('Please input your first meter reading in cubic meters: ') #example 45
        final = input('Please input your final meter reading in cubic meters: ') #example 678
        days = input('Please input how many days it has been: ') #example 30
        return restart(first, final, days)
    elif n == 17:
        print 'This program will calculate your monthly morgage intrest rates.'
        raw_input('Press Enter to continue...')
        P = input('Please insert your initial principal (loan ammount) without the "$" sign: ') #example $20,000
        rate = input('Please insert your annual intrest rate as a percentage without the "%" sign: ') #7.5
        years = input('Please insert how many years are in your amortization period: ') #Example 5 years
        return Morgage(P, rate, years)
    else:
        print 'You have encountered an error.\nPlease make sure you selected a valid option.\n\n\n'
        time.sleep(1)
        return restart()

def idiot_check(n):
    if n > 17:
        print 'You did not input a valid number, please try again.\n\n\n'
        time.sleep(1)
        return restart()
    elif n < 1:
        print 'You did not input a valid number, please try again.\n\n\n'
        time.sleep(1)
        return restart()
    elif 18 > n > 0:
        print 'Your input was accepted.'
        time.sleep(1)
        return selected_option(n)
    else:
        print 'error'
        time.sleep(2)
        return restart()
    
def start():  # start of the program. first def to be run
    print "Please select one of the following options:"
    time.sleep(1)
    print "#1 --  Convert Celsius to Fahrenheit."
    print "#2 --  Convert Fahrenheit to Celsius."
    print "#3 --  Calculate the Area of a Square."
    print "#4 --  Calculate the Area of a Rectangle."
    print "#5 --  Calculate the Area of a Right Angled Triangle."
    print "#6 --  Calculate the Hypotenuse of a Right Angled Triangle."
    print "#7 --  Calculate the Circumference of a Circle."
    print "#8 --  Calculate the Area of a Circle."
    print "#9 --  Convert a Fraction to a Decimal."
    print "#10 -  Calculate the Average of 3 Numbers."
    print "#11 -  Calculate 2 Numbers, give Sum, Product, & Remainder."
    print "#12 -  Calculate Fuel Consumption and Average on Journey."
    print "#13 -  Convert Canadian Currency to US."
    print "#14 -  Calculate your BMI in metric."
    print "#15 -  Calculate the Hull Speed of a Boat."
    print "#16 -  Calculate a Gas Bill."
    print "#17 -  Calculate a Mortgage's Intrest."
    print "--------------------------------------------------------------"
    n = input('Please select an option now: ') 
    return idiot_check(n) # checks to see if the user is retarded.

start()