class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        # values are sorted now, so if first two match, they are the same and can be removed
        while len(nums) > 1:
            if nums[0] == nums[1]:
                nums.remove(nums[0])
                nums.remove(nums[0])
                # print(nums)
            else:
                return nums[0]
        return nums[0]
