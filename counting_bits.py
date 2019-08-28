# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         ans, total = [], []
#         for num in range(num + 1):
#             ans.append(str(bin(num)))
#         for val in ans:
#             total.append(val.count('1'))
#         return total


class Solution:
    def countBits(self, num: int) -> List[int]:
        ans, total = [], []
        for num in range(num + 1):
            total.append(bin(num)).count('1')
        return total
