from Stack import Stack
import re
 
def infixToPostfix(infixexpr):
    # Create a Dictionary to store the precedence of operators
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    # Create a stack to hold operators
    opStack = Stack()
    # Create a list to hold the PostFix expression
    postfixList = []
    # allows multiplication by sequential parenthetical groups
    infixexpr = re.sub("\)[\s]*\(", ")*(", infixexpr)

    # Split the infix expression into a list of tokens
    tokenList = [x for x in infixexpr if x != " "]

    # Loop through the tokens
    for token in tokenList:
        # If it is a letter or a number
        if token.isalpha() or token.isdecimal() or token in ".":

            # Append to the PostFix list
            postfixList.append(token)
        # If it is an opening parenthesis
        elif token == '(':
            # Push onto the stack to wait for closing parenthesis
            opStack.push(token)
        # If it is a closing parenthesis
        elif token == ')':
            # Pop the top of the stack
            topToken = opStack.pop()
            # Loop until we reach the opening parenthesis
            while topToken != '(':
                # Append the token to the PostFix list with space before
                postfixList.append(" " + topToken)

                # Pop the stack
                topToken = opStack.pop()
        # The token is not a letter or number
        else:
            # Loop while the stack isn't empty AND
            # the top of the stack has greater than equal
            # precedence than the current token
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                # Pop the stack and append to the PostFix    
                postfixList.append(opStack.pop())

           #creates space between operands and operators
            postfixList.append(" ")
             # Push the current token to the stack
            opStack.push(token)

    # Loop through the stack until it is empty 
    while not opStack.isEmpty():
        # Append to the PostFix list
        #adds space between all operands and operators
        postfixList.append(" " + opStack.pop())
        print(postfixList)

    # Return the Postfix List with spaces between each item
    return "".join(postfixList)

# print("Infix:   " + "AA * B + C * D")
# print("Postfix: " + infixToPostfix("AA * B + C * D"))
# print("Infix:   " + "( A + B ) * C - ( D - E ) * ( F + G )")
# print("Postfix: " + infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
