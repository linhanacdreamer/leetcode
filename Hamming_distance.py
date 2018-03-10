'''
count the number of 1 in the result of  x^y
        return bin(x^y).count('1')                # bin() 返回一个整数 int 或者长整数 long int 的二进制  '0b1010'
        return len([i for i in format(x ^ y, 'b') if i=='1'])  *format 格式化方法
        return bin(x ^ y)[2:].count('1')
        len(’’.join(str(bin(x^y)).split(‘0’)))-1
------  y表示0或者1中的某一个
        对于奇数来说 m&(m-1) = m-1
             假设x二进制表示为1yyyyyyy1
             x - 1二进制表示为1yyyyyyy0
          此时 m&(m-1)的结果为1yyyyyyy0（去掉了一个最后一个1）
        对于偶数来说 m&(m-1) : m-1 的
            假设x二进制表示为1yyyyyyy1000000
            x - 1二进制表示为1yyyyyyy0111111
         此时 m&(m-1)的结果为1yyyyyyy0000000（去掉了最后一个1）
        总结：每次m&(m-1)都会去掉一个1
        m = x ^ y
        n = 0
        while(m):
            n += 1
            m &= m -1
        return n
        --------------
        target = x ^ y
        return Solution.count_ones(target)

        @staticmethod
        def round(num, mask, c):
        return (num & mask) + (num >> (1 << c) & mask)

        @staticmethod
        def count_ones(num):
        num = Solution.round(num, 0x55555555, 0)
        num = Solution.round(num, 0x33333333, 1)
        num = Solution.round(num, 0x0f0f0f0f, 2)
        num = Solution.round(num, 0x00ff00ff, 3)
        num = Solution.round(num, 0x0000ffff, 4)
        return num
'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = x ^ y
        count = 0
        while(ans > 0):
            if ans % 2 > 0 :
                count += 1
            ans>>=1
        return count