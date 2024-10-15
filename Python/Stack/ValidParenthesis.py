# define a function to check for valid parenthesis

def is_valid_parenthesis(s):
    stack = []

    for char in s:

        # opening the bracket
        if char in '({[':
            stack.append(char)
        
        # closing the bracket

        if char in ')}]':
            pass



