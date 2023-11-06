class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_dict = {}
        missing, duplicate = 0, 0

    # Populate the dictionary with counts
        for num in nums:
            if num in num_dict:
                duplicate = num
            num_dict[num] = num_dict.get(num, 0) + 1

    # Find the missing number
        for i in range(1, len(nums) + 1):
            if i not in num_dict:
                missing = i

        return [duplicate, missing]