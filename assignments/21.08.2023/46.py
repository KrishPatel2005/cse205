class Solution:
    def permute(self, li):
        result = []

        def backtrack(current_permutation):
            if(len(current_permutation)==len(li)):
                result.append(list(current_permutation))
                return
            
            for num in li:
                if num not in current_permutation:
                    current_permutation.append(num)
                    backtrack(current_permutation)
                    current_permutation.pop()
            
        backtrack([])
        return result
s = Solution()
k = s.permute([1,2,3])
print(k)