'''
['FizzBuzz'[i%-3&-4:i%-5&8^12]or`i`for i in range(1,n+1)]

['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

str(i) * (i % 3 != 0 and i % 5 != 0) + "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)
                for i in range(1, n + 1)]

['Fizz'*(i%3/2)+'Buzz'*(i%5/4)or`i+1`for i in range(n)]

[str(i) if (i%3!=0 and i%5!=0) else (('Fizz'*(i%3==0)) + ('Buzz'*(i%5==0))) for i in range(1,n+1)]



'''
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        for x in range(1,n+1):
            if x % 15 == 0:
                list.append("FizzBuzz")
            elif x % 5 ==0:
                list.append("Buzz")
            elif x % 3 ==0:
                list.append("Fizz")
            else:
                list.append(str(x))
        return list