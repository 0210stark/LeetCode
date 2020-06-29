class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        l = 0
        c = 0
        for char in s:
            if char == 'L':
                l += 1
            if char == 'R':
                r += 1
            if l == r:
                c += 1
        return c
