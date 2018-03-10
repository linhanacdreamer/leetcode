'''count the letter of S in J
map:map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回.
str.count(substr,star,end)  : 表示substr在str中在star和end之间出现的次数
solution 1:
def numJewelsInStones(self, J, S):
    return sum(map(J.count, S))               #计算S中的每个元素在J中出现次数总和。
def numJewelsInStones(self, J, S):            没想到
    return sum(map(S.count, J))               #计算J中的每个元素在S中出现的次数总和
def numJewelsInStones(self, J, S):
    return sum(s in J for s in S)
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

