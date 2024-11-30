# https://leetcode.com/problems/valid-parentheses/

# Approach:
# Create a hashmap with correct closing parenthesis for the corrosponding opening paranthesis
# Create a stack
# Iterate through s and for each parenthesis:
# If opening, push it to the stack
# If closing, pop from stack and check if they match (hashmap), return False if not
# At the end, check if stack is empty or not
# Return the result
# Time O(n) | Space O(n)

def isValid(s):
    parenthesis = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for ch in s:
        if ch in parenthesis:
            stack.append(ch)
            continue
        if not stack:
            return False
        opening = stack.pop()
        if parenthesis[opening] != ch:
            return False
    return len(stack) == 0
        
# s = "()[]{}"
# s = "(]"
s = "[[[[[[["
print(isValid(s))