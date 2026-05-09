class Solution:

    def encode(self, strs: List[str]) -> str:
        # take the number of elements and add that to the delimeter
        s = ''
        for string in strs:
            n = len(string)
            s += f"{n}#{string}"

        return s
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            n = int(s[i:j])
            res.append("")

            for k in range(j + 1, j + n + 1):
                res[-1] += s[k]
            
            i = j + n + 1

        return res

