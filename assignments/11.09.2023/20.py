class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty stack to store open brackets
        
        # Define a dictionary to store the mapping of open and close brackets
        bracket_mapping = {')': '(', '}': '{', ']': '['}
        
        # Iterate through the characters in the string
        for char in s:
            # If the character is an open bracket, push it onto the stack
            if char in bracket_mapping.values():
                stack.append(char)
            else:
                # If the character is a close bracket, check if the stack is empty or if the top element doesn't match
                if not stack or bracket_mapping[char] != stack.pop():
                    return False  # Invalid string
        
        # After iterating through the string, the stack should be empty if the string is valid
        return not stack