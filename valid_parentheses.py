class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            t = s
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
            if s == t:
                return False
        return True
