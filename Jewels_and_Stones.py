'''count the letter of S in J
solution 1:
def numJewelsInStones(self, J, S):
    return sum(map(J.count, S))
def numJewelsInStones(self, J, S):
    return sum(map(S.count, J))               # this one after seeing https://discuss.leetcode.com/post/244105
def numJewelsInStones(self, J, S):
    return sum(s in J for s in S)
solution 3:
def numJewelsInStones(self, J, S):
        stones = Counter(S)
        return sum([stones[s] for s in stones.keys() if s in set(J)])
'''
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for le in S:
            if le in J:
                count+=1
        return count

