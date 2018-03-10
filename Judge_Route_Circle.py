'''
a robot can return
--------  collections.Counter(moves)  : 跟踪moves里面的字符的出现次数
    c = collections.Counter(moves)
    return c['L'] == c['R'] and c['U'] == c['D']
--------   学习这种使用
    return not sum(map({'U': 1, 'D': -1, 'L': 1j, 'R': -1j}.get, moves))
--------
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
--------  python 有 实数和虚数
    direct = {'U': 1, 'D': -1, 'L': 1j, 'R': -1j}
    return 0 == sum(direct[m] for m in moves)
'''
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return (moves.count('L') ^ moves.count('R') or moves.count('D') ^ moves.count('U')) == 0
