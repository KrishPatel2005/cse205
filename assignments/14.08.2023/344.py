class Solution:
    def reversStr(self, a, b, c):
        if (a>=b//2):
            return
        c[a], c[b - 1 - a] = c[b - 1 - a], c[a]
        self.reversStr(a + 1, b, c)

    def reverseString(self, c):
        b = len(c)
        self.reversStr(0, b, c)