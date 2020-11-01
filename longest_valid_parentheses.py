class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        
        for i, bracket in enumerate(s):
            if bracket == '(':
                stack.append(i)
            else:
                stack.pop()
                if (not stack):
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
                    
        return ans
