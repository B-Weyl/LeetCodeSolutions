class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd, even = [], []
        for val in A:
            if val % 2 == 0:
                even.append(val)
            else:
                odd.append(val)
        return even + odd
