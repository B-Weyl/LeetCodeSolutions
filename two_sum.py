class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = 0
        for value in nums:
            y = target - value
            x += 1
            remainder = nums[x:]
            if y in remainder:
                return [x - 1, remainder.index(y) + x]


if __name__ == '__main__':
    print(Solution().twoSum((2, 7, 11, 15), 9))
