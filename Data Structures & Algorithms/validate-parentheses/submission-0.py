class Solution:
    def isValid(self, s: str) -> bool:
        BRACKET_PAIRS = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for c in s:
            if c in BRACKET_PAIRS.keys():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                val = stack.pop()

                if BRACKET_PAIRS[val] != c:
                    return False

        if len(stack) != 0:
            return False

        return True
