class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n, m = len(version1), len(version2)
        p1 = p2 = 0

        while p1 < n or p2 < m:
            rev1 = 0
            while p1 < n and version1[p1] != ".":
                rev1 *= 10
                rev1 += int(version1[p1])
                p1 += 1
            
            rev2 = 0
            while p2 < m and version2[p2] != ".":
                rev2 *= 10
                rev2 += int(version2[p2])
                p2 += 1
            
            if rev1 > rev2:
                return 1
            elif rev1 < rev2:
                return -1
            
            p1 += 1
            p2 += 1

        return 0