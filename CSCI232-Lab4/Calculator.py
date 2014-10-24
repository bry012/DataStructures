__author__ = 'bryan'
from infixToPostfix import infixToPostfix
from postfixEvaluator import postfixEval
from postfixEvaluator import doMath

def menuPrompt():
    equation = input("Please enter in your equation or type 'exit' to exit the program:")

    if equation.strip() == "exit":
        return False
    elif equation.strip() == "":
        print("Please enter in an equation")
        return True
    else:
        try:
            print("Answer: " + str(postfixEval(infixToPostfix(equation))))
        except Exception as e:
            print("Invalid Equation: " + equation)
        return True


def main():
    resume = True
    print("Welcome to Calculator App! \nThis calculator currently can handle multiple operations while following order of operations.")
    while resume:
        resume = menuPrompt()


main()