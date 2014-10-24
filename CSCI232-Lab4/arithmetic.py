__author__ = 'bryan'

def add(firstNum, secondNum):
    try:
        return firstNum + secondNum

    except(TypeError) as error:
        print("Please enter in an int or float for your operands")

def subtract(firstNum,secondNum):
    try:
        return firstNum - secondNum

    except(TypeError) as error:
        print("Please enter in an int or float for your operands")

def multiply(firstNum,secondNum):
    try:

        return firstNum * secondNum

    except(TypeError) as error:
        print("Please enter in an int or float for your operands")

def power(firstNum,secondNum):
    try:
        return firstNum ** secondNum

    except(TypeError) as error:
        print("Please enter in an int or float for your operands")

def divide(firstNum,secondNum):
    try:
        if type(firstNum) is int and type(secondNum) is int:
            return firstNum // secondNum
        else:
            return firstNum / secondNum

    except(TypeError,ZeroDivisionError) as error:
        if type(error) is TypeError:
            print("Please enter in an int or float for your operands")

        if type(error) is ZeroDivisionError:
            print("Cannot divide by zero")

def convertStr(num):
    try:
        return int(num)
    except ValueError as error:
        try:
            return float(num)
        except ValueError as error:
            return None



if __name__ == "__main__":

    ints = []
    floats = []
    ints.extend([add(4,12),subtract(4,12),multiply(4,12),divide(4,12)])
    floats.extend([add(3.5,1.2),subtract(3.5,1.2),multiply(3.5,1.2),divide(3.5,1.2)])

    for nums in ints:
        print(nums)

    for nums in floats:
        print(nums)

    divide(12,0)

