class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''

        for word in strs:
            s = s + '#' + f"{len(word)}" + '#' + word
            
        return s

        

    def decode(self, s: str) -> List[str]:
        print(s)
        result = []

        i = 0

        while i < len(s):
            if s[i] == '#':
                i += 1 # currently we see # so increase to get number
                letter_count = ''

                while s[i] != '#':
                    letter_count += s[i]
                    i += 1
                
                letter_count = int(letter_count)

                i += 1
                word = ""

                j = i + letter_count

                while i < len(s) and i < j:
                    word += s[i]
                    i += 1
                
                result.append(word)
            else:
                i += 1
            

        return result
