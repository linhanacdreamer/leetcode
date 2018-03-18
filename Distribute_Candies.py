'''
min(len(candies)//2 ,len(set(candies)))

'''
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        leng = len(set(candies))
        return ( len(candies)//2 if leng > len(candies)//2 else leng )