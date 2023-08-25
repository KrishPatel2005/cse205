class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, current_subset):
            result.append(list(current_subset))  # Add the current subset to the result
            
            # Iterate through the remaining elements
            for i in range(start, len(nums)):
                current_subset.append(nums[i])  # Include the current element in the subset
                backtrack(i + 1, current_subset)  # Recurse with the next index
                current_subset.pop()  # Backtrack by removing the last element

        result = []
        backtrack(0, [])
        return result
        