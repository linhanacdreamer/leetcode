'''
num ^ ((1<<num.bit_length())-1)
num ^ ((1 << len(bin(num)) - 2) - 1)
num ^ ((2<<int(math.log(num, 2)))-1)
num ^ ((2<<int(math.log(num, 2)))-1)
~num & ((1<<num.bit_length())-1)
int("".join( [ "1" if ls == "0" else "0" for ls in "{0:b}".format(num) ] ), 2)
num ^ int('1'*len(bin(num)[2:]),2)
int(''.join(map(lambda x: str(int(not int(x))), bin(num)[2:])), 2)
'''
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(('1'*bin(num)[2:].__len__()),2)^num