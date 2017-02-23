class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            x = str(x)
        else:
            return False
        for i in range(int(round(len(x)))):
            if x[i] != x[-i - 1]:
                return False
        return True