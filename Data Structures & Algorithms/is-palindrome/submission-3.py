class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer
        # have a l and r and skip any non alphanum
        # if we reach l >= r then return true

        l = 0
        r = len(s) - 1

        while l < r:
            while l < len(s) and not s[l].isalnum():
                l += 1

            while r >= 0 and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1



        return True
        