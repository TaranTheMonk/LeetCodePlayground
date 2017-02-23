class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if target > nums[i]:
                try:
                    if nums[i + 1] > target:
                        return i + 1
                except:
                    return i + 1
        return 0