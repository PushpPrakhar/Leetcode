class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m= {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        stack=[]

        for character in s:
            if character in '([{':
                stack.append(character)
            elif stack and character == m[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
