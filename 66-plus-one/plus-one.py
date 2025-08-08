class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=str(digits)
        digits=digits.replace(" ","").replace(",","").replace("[","").replace("]","")
        digits=int(digits)+1
        digits=str(digits)
        digits=[int(digit)for digit in digits]
        return digits



