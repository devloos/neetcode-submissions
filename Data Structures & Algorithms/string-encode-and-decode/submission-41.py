class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '#_$@)@_)-----'
        return '#_$@)@_)'.join(strs)
    def decode(self, s: str) -> List[str]:
        if s == '#_$@)@_)-----':
            return []
        if s == '':
            return ['']
        return s.split('#_$@)@_)')