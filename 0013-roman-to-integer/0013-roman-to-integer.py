class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        new=0
        i = 0;
        ihate = {'I': 1,'IV': 4,'V': 5, 'IX': 9, 'X': 10,'XL': 40, 'XC':90,'L':50,'C':100,'CD': 400,'CM': 900,'D': 500,'M': 1000}


        while i < len(s):
            if s[i:i+2] in ihate:
                new += ihate[s[i:i+2]]
                i += 2
            else:
                new += ihate[s[i]]
                i += 1

        return(new)

                


        