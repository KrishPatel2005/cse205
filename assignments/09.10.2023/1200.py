class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff = float('inf')
        res = []

        for i in range(1, len (arr)):
            diff = arr[i]-arr[i-1]
            if min_diff > diff:
                min_diff = diff
                res = [[arr[i-1], arr[i]]]
            elif min_diff == diff:
                res.append([arr[i-1],arr[i]])
        
        return res