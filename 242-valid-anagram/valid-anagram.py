class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s={} #declare dictnory for s 
        dic_t={} #declare dictnory for t
        for i in s: 
            if i in dic_s:
                dic_s[i]+=1
            else:
                dic_s[i]=1
        for i in t:
            if i in dic_t:
                dic_t[i]+=1
            else:
                dic_t[i]=1
        if dic_t==dic_s: #if both dictnory have same key values return True
            return True 
        else:
            return False
