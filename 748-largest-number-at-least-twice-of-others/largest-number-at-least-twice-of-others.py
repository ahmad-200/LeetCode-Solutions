class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0
        for i in range(len(nums)):
         if nums[i]>nums[max]:
            max=i
        else :
            pass

        for i in range(len(nums)):
            if i==max:
                continue
            if nums[i]*2>nums[max]:
                return -1

        return max