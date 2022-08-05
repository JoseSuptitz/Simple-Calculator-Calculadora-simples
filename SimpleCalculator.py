def number1():
    while True:
        numberOne = int(input("""
----------------------------------------------------------
Welcome to the calculator! Please insert the first number:
----------------------------------------------------------
"""))  
        return numberOne      

def number2():
    while True:
        numberTwo = int(input("""
-------------------------
Insert the second number:
-------------------------
"""))
        return numberTwo
   

def operators():
    operation = input('Do you want: + (addition), - (subtraction), * (multiplication) or / (division): ')
    return operation

def addition(numberOne, numberTwo):
    return numberOne + numberTwo

def subtraction(numberOne, numberTwo):    
    return numberOne - numberTwo

def multiplication(numberOne, numberTwo):
    return numberOne * numberTwo

def division(numberOne, numberTwo):
    return numberOne / numberTwo

while True:
    
    #Gets numbers and type of operator
    numberOne = number1()
    numberTwo = number2()
    operation = operators()

    #Each If statement is a operation that calls its respective function.        
    if(operation == '+'):
        sumTwoNum = addition(numberOne, numberTwo)
        print('\nYour number is: ', sumTwoNum, '\n')
        
    elif(operation == '-'):
        subTwoNum = subtraction(numberOne, numberTwo)
        print('\nYour number is: ', subTwoNum, '\n')

    elif(operation == '*'):  
        mulTwoNum = multiplication(numberOne, numberTwo)
        print('\nYour number is: ', mulTwoNum, '\n')

    elif(operation == '/'):           
        divTwoNum = division(numberOne, numberTwo)
        print('\nYour number is: ', divTwoNum, '\n')

    else:
        print('\nDefine a a real operator.\n')    

    #Asks if the user wants to keep using the calculator.
    keepGoing = input('Do you want to continue? (Y/N)')
    if(keepGoing.upper() == 'N'):
        break
    else:
        continue