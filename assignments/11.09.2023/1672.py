class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        li=[]
        for i in accounts:
            sum=0
            for j in i:
                sum = sum+j
            li.append(sum)
        li.sort()
        li.reverse()
        return li[0]   