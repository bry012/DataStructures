__author__ = 'bryan'

import arithmetic,re

def convertStr(num):
    try:
        return int(num)
    except ValueError as error:
        try:
            return float(num)
        except ValueError as error:
            return None

def evaluateEqaution(operands,operators):

    if operators[0] == "+":
        return arithmetic.add(operands[0],operands[1])
    elif operators[0] == "-":
        return arithmetic.subtract(operands[0],operands[1])
    elif operators[0] == "*":
        return arithmetic.multiply(operands[0],operands[1])
    elif operators[0] == "/":
        return arithmetic.divide(operands[0],operands[1])
    elif operators == "^":
        return  arithmetic.power(operands[0],operands[1])


def editOps(operands,operators,operator):
        operatorIndex = operators.index(operator)
        operandsList = [operands[operatorIndex],operands[operatorIndex + 1]]
        newVal = evaluateEqaution(operandsList,operator)
        del operands[operatorIndex:operatorIndex + 2]
        del operators[operatorIndex]
        operands.insert(operatorIndex,newVal)


def orderOfOps(operands,operators):

    #if only 2 operands remain, return the final answer
    if len(operands) == 2:
       answer =  evaluateEqaution(operands,operators[0])
       return answer

    elif "^" in operators:
        editOps(operands,operators,"^")
        return orderOfOps(operands,operators)

    elif "*" in operators:
        editOps(operands,operators,"*")
        return orderOfOps(operands,operators)

    elif "/" in operators:
        editOps(operands,operators,"/")
        return orderOfOps(operands,operators)

    elif "+" in operators:
        editOps(operands,operators,"+")
        return orderOfOps(operands,operators)

    elif "-" in operators:
        editOps(operands,operators,"-")
        return orderOfOps(operands,operators)



def parseEquation(equation):
    #removes extra whitspace
    equation = re.sub("\s", "", equation)
    operands = re.split("[\+\-\*/\^]", equation)
    operators = re.findall("[\+\-\*/\^]", equation)
    #if multiple operators are in a row, empty strings will appear in the operands list signifying
    #a invalid equation
    if "" in operands:
        print("invalid equation")

    else:
        validOperands = True
        for val in operands:
            convertedVal = convertStr(val)
            if convertedVal == None:
                validOperands = False
                print("Invalid Operand: " + val)


        if validOperands:
            convertedOperands = [convertStr(num) for num in operands]
            print("valid: " + equation)
            print("Answer: " + str(orderOfOps(convertedOperands,operators)))


def menuPrompt():
    equation = input("Please enter in your equation or type 'exit' to exit the program:")

    if equation.strip() == "exit":
        return False
    else:
        parseEquation(equation)
        return True


def main():
    resume = True
    print("Welcome to Calculator App! \nThis calculator currently can handle multiple operations while following order of operations.")
    while resume:
        resume = menuPrompt()

if __name__ == "__main__":
    main()



