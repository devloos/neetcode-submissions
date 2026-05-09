class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        s = dict()

        for num in nums:
            if num in s:
                return True

            s[num] = 1

        return False
