class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #ahmad-200
        words=s.split()
        return(len(words[-1]))
        


