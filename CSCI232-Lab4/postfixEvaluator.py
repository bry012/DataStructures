from Stack import Stack
from infixToPostfix import infixToPostfix
import arithmetic
import re
 
def postfixEval(postfixExpr):
    # Create a Stack to hold the operands

    operandStack = Stack()
    # Create a list of all the tokens in the expression
    tokenList = postfixExpr.split(" ")


    # Loop through the tokens in the list
    for token in tokenList:
        # if it is a number
        convertedNum = arithmetic.convertStr(token)
        if convertedNum:
            # Cast the number to an int and push onto stack
            operandStack.push(convertedNum)
        # The token is not a number
        else:
            # Pop the stack twice to get the two operators
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            # Perform the math calculation
            result = doMath(token,operand1,operand2)
            # Push the result back to the stack
            operandStack.push(result)
    # Return the last item on the stack
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return arithmetic.multiply(op1,op2)
    elif op == "/":
        return arithmetic.divide(op1,op2)
    elif op == "+":
        return arithmetic.add(op1,op2)
    elif op == "^":
        return arithmetic.power(op1,op2)
    else:
        return arithmetic.subtract(op1,op2)


# print(postfixEval(infixToPostfix('(5+(12 + 5))/ (7.0 -1)')))
