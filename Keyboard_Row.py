'''
filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)
[word for word in words if any(set(word.upper()).issubset(row) for row in [set('QWERTYUIOP'), set('ASDFGHJKL'), set('ZXCVBNM')])]

        r1 = 'qwertyuiop'
        r2 = 'asdfghjkl'
        r3 = 'zxcvbnm'
        [word for word in words if set(word.lower()) <= set(r1) or set(word.lower()) <= set(r2) or set(word.lower()) <= set(r3)]

listSets = [set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")]
[str for str in words for row in listSets if set(str.lower()) <= row]
'''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        list1 = ['q','w','e','r','t','y','u','i','o','p']
        list2 = ['a','s','d','f','g','h','j','k','l']
        list3 = ['z','x','c','v','b','n','m']
        dict1 = dict( (x,1) for x in list1)
        dict1.update(dict( (x,2) for x in list2))
        dict1.update(dict( (x,3) for x in list3))
        return [str for str in words if len(str)*dict1.get(str[0].lower()) == sum([dict1.get(x) for x in str.lower()]) ]
