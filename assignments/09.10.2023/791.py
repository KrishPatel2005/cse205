class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s1 = Counter(s)
        o1 = Counter(order)

        res = ""

        for i in order:
            if i in s1:
                res += i*s1[i]
        for i in s:
            if i not in o1:
                res += i
        
        return res