# The shunting yard algorithm is used to convert an infix expression into postfix

def shuntingYard(infixExpression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2} # Set the precedence of each operator
    
    operatorStack = [] # Stores the operators and parentheses
    output = [] # Stores the postfix to be returned
    
    tokenized = infixExpression.replace(" ", "") # Remove any spaces
    
    for token in tokenized:
        if token.isdigit():
            output.append(token) # If the token is a digit it goes directly to the output
        elif token in precedence: # If the token is an operator...
            while (
                len(operatorStack) != 0 and # Check if there is no more operators to process
                operatorStack[-1] != "(" and # Ensure the loop continues until the opening parenthesis is found
                precedence[token] <= precedence.get(operatorStack[-1], 0) # 0 is used as the default precedence if the operator is not found in the dict
            ):
                # While there are operators on the stack and the top operator has a higher precedence, pop it and append it to the output
                output.append(operatorStack.pop())
            operatorStack.append(token) # Push the current operator onto the stack as it has a higher precedence
        elif token == "(":
            # If the token is an opening parenthesis, push it to the stack (used as a marker)
            operatorStack.append(token)
        elif token == ")":
            # If the token is a closing parenthesis...
            while len(operatorStack) != 0 and operatorStack[-1] != "(":
                # Pop operators from the stack and append to the output until the opening parenthesis is found
                output.append(operatorStack.pop())
            if len(operatorStack) != 0 and operatorStack[-1] == "(":
                # If the opening parenthesis is found, discard it
                operatorStack.pop()
        
    while len(operatorStack) != 0: # Pop the remaining operators from the stack and append to the output
        output.append(operatorStack.pop())
    
    return "".join(output) # Join the output list together into a string

expression = "8 - 4 / (2 + 1)"
print(shuntingYard(expression))