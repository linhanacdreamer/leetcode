'''
return [i for i in range(left,right+1) if all(int(x) != 0 and (i % int(x)) == 0 for x in str(i))]

is_self_dividing = lambda num: '0' not in str(num) and all([num % int(digit) == 0 for digit in str(num)])
return filter(is_self_dividing, range(left, right + 1))

output = []
for num in range(left, right+1):
    num_str = str(num)
    for c in num_str:
        if c == '0':
            break
        if num%int(c) != 0:
            break
    else:
        output.append(num)
return output

return [number for number in range(left, right+1) if '0' not in str(number) and all((number % int(char) == 0 for char in str(number)))]

return [num for num in range(left, right+1) if all((int(d) and not num % int(d)) for d in str(num))]
'''
class Solution(object):
    def selfDividingNumbers(self, left, right):
        list = []
        for x in range(left,right+1):
            if x % 10 == 0:
                continue
            y = x
            while y:
                c = y % 10
                if not c :
                    break
                if x % c == 0:
                    y/=10
                    continue
                else:
                    break
            if not y:
                list.append(x)
        return list