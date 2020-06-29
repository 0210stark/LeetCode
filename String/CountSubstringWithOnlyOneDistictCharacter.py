import itertools


class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        r = 0
        for _, group in itertools.groupby(S):
            l = len(list(group))
            r += l * (l+1)/2

        return r
