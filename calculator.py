print("<<<<<-----------Calculator----------->>>>>")

# function for addition
def addition(a, b):
    return (a + b)

# function for subtraction
def subtraction(a, b):
    return (a - b)

# function for multiplication
def multiplication(a, b):
    return (a * b)

# function for division
def division(a, b):
    # division by zero is not possible
    if (b == 0):
        print("Division by zero is not possible!!!!!")
    else:
        return (a / b)

# function for modulo
def modulo(a, b):
    # division by zero is not possible
    if (b == 0):
        print("Division by zero is not possible!!!!!")
    else:
        return (a % b)

print("-----------------------------------------------")
print("Enter i if you want to input a integer value")
print("Enter f if you want to input a float value")
print("-----------------------------------------------")
print("Enter '+' for addition")
print("Enter '-' for subtraction")
print("Enter '*' for addition")
print("Enter '/' for addition")
print("Enter '%' for addition")
print("-----------------------------------------------")
choice1 = str(input("Enter the choice for integer or float(i or I or f or F): "))
choice2 = str(input("Enter your choice for arthmetic operation(+,/,*,-,%): "))
print("-----------------------------------------------")
# if user chooses i or I then this condition is true
if(choice1 == 'i' or choice1 == 'I'):
    a1 = (input("Enter the first integer: "))
    # checking for invalid input using ascii values
    # for loop is used to check if there is a invalid input given by the user
    # for loop is used to check multiple characters
    for i in a1:
        # the ascii values of 0 to 9 is from 48 to 57 so except these values all the other values are invalid to be considered as a integer        
        # '.'(ascii value = 46) is invalid for a integer but valid for float
        if(0 <= ord(i) and 47 >= ord(i)):
        # one thing to keep in mind is that '-'(ascii value = 45) and '+'(ascii value = 43) can also be accepted as integer & float if they are at correct position i.e. at the beginning of any number for example: -8,-96,+96 are all valid but 8-,96+ are invalid    
            if(a1[0] == '-' or a1[0] == '+'):
            # if the above condition is true then use the continue statement 
                if(ord(i) == 45 or ord(i) == 43):
                    continue
            print("Invalid Input!!!")
            exit()
        elif(58 <= ord(i) and 127 >= ord(i)):
            # if this condition is true the exit the program
            print("Invalid Input!!!")
            exit()
    # convert the valid string into integer
    a1 = int(a1)
    # the same process goes for second variable
    b1 = (input("Enter the second integer: "))
    print("-----------------------------------------------")
    for j in b1:
        if(0 <= ord(j) and 47 >= ord(j)):
            if(b1[0] == '-' or b1[0] == '+'):
                if(ord(j) == 45 or ord(j) == 43):
                    continue
            print("Invalid Input!!!")
            exit()
        elif(58 <= ord(j) and 127 >= ord(j)):
            print("Invalid Input!!!")
            exit()    
    b1 = int(b1)
    # the choice for arthmetic operation is given by the user so use the appropriate function according to the operator  
    if(choice2 == '+'):
        print(a1, "+", b1, "=", addition(a1, b1))
    elif(choice2 == '-'):
        print(a1, "-", b1, "=", subtraction(a1, b1))
    elif(choice2 == '*'):
        print(a1, "*", b1, "=", multiplication(a1, b1))
    elif(choice2 == '/'):
        # this condition is for zero division
        if(b1 == 0):
            division(a1, b1)
        else:
            print(a1, "/", b1, "=", division(a1, b1))

    elif(choice2 == '%'):
        # this condition is for zero division
        if(b1 == 0):
            modulo(a1, b1)
        else:
            print(a1, "%", b1, "=", modulo(a1, b1))
# if user chooses f or F then this condition is true
# all the conditions is same as of integer just keep in mind that '.'(ascii value = 46) is valid in float 
elif(choice1 == 'f' or choice1 == 'F'):
    a2 = (input("Enter the first integer: "))
    for k in a2:
        if(0 <= ord(k) and 47 >= ord(k)):
            if(a2[0] == '-' or a2[0] == '+'):
                if(ord(k) == 45 or ord(k) == 43):
                    continue
            if(ord(k) == 46):
                continue
            print("Invalid Input!!!")
            exit()
        elif(58 <= ord(k) and 127 >= ord(k)):
            print("Invalid Input!!!")
            exit()
    a2 = float(a2)
    b2 = (input("Enter the second integer: "))
    print("-----------------------------------------------")
    for l in b2:
        if(0 <= ord(l) and 47 >= ord(l)):
            if(b2[0] == '-' or b2[0] == '+'):
                if(ord(l) == 45 or ord(l) == 43):
                    continue
            if(ord(l) == 46):
                continue
            print("Invalid Input!!!")
            exit()
        elif(58 <= ord(l) and 127 >= ord(l)):
            print("Invalid Input!!!")
            exit()
    b2 = float(b2)
    if(choice2 == '+'):
        print(a2, "+", b2, "=", addition(a2, b2))
    elif(choice2 == '-'):
        print(a2, "-", b2, "=", subtraction(a2, b2))
    elif(choice2 == '*'):
        print(a2, "*", b2, "=", multiplication(a2, b2))
    elif(choice2 == '/'):
        if(b2 == 0):
            division(a2, b2)
        else:
            print(a2, "/", b2, "=", division(a2, b2))
    elif(choice2 == '%'):
        if(b2 == 0):
            modulo(a2, b2)
        else:
            print(a2, "%", b2, "=", modulo(a2, b2))
# if user nither chooses i or I or f or F then print a message
else:
    print("Invalid Input!!!")
# by Tushar Singh