def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for char in s:
            if char == '(':
                # Start a new nesting level
                stack.append(0)
            else:
                # Close the current nesting level
                inner_score = stack.pop()
                # If score is 0, it was '()', which equals 1.
                # If score > 0, it was '(A)', which equals 2 * score.
                val = max(2 * inner_score, 1)
                # Add to the outer level
                stack[-1] += val
        
        return stack[0]
