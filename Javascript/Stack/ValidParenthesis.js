const isValidParenthesis = (s) => {
    let stack = []

    for (let i=0; i<stack.length; i++) {
        
        if (s[i] === '(' || s[i] === '{' || s[i] === '[') {
            stack.push(stack[i])
        } else {
            // if its's a closing bracket, check if the stack is non-empty
            // and if the top of the stack is a matching opening bracket
            if (stack.length > 0 && 
                ((stack[stack.length -1] === '(' && s[i] === ')')) || 
                ((stack[stack.length -1] === '{' && s[i] === '}')) || 
                ((stack[stack.length -1] === '[' && s[i] === ']'))
            ) {
                stack.pop() // Pop the matching opening bracket
            } else {
                return false  // Unmatched closing bracket
            }
        }
    }

    // If stack is empty, return true (balanced), otherwise false
    return stack.length === 0;
}

let s = "{()}[]";

console.log(isValidParenthesis(s) ? "Valid Parenthesis" : "Invalid Parenthesis")

