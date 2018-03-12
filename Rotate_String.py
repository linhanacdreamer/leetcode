'''
better
return len(A) == len(B) and B in A + A
'''
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return ((B in A + A) if B.__len__() > 0 else False)
