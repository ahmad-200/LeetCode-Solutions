class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if (i not in d.keys()):
                d[i]=1
            else:
                d[i]+=1
        for value in d:
            if d[value]==1:
                return value

            
                