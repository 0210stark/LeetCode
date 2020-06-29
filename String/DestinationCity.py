class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        pairs = {points[0]: points[1] for points in paths}
        for src, dest in pairs.items():
            if dest not in pairs:
                return dest
