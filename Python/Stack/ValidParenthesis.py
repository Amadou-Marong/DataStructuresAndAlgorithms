# define a function to check for valid parenthesis

def is_valid_parenthesis(s):
    stack = []

    for char in s:

        # opening the bracket
        if char in '({[':
            stack.append(char)
        
        # closing the bracket

        if char in ')}]':
            
            # closing bracket without opening
            if not stack:
                return False
            
            # else pop an item check for matching
            top = stack.pop()

            if (top == '(' and char != ')') or \
                (top == '{' and char != '}') or \
                (top == '[' and char != ']'):
                return False
            
    # if an opening bracket without closing
    return len(stack) == 0


# example
s = '{()}[]'

if is_valid_parenthesis(s):
    print("Valid Parenthesis")
else:
    print("Invalid Parenthesis")


            




