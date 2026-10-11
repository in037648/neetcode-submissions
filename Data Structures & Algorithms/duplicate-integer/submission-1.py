class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        # num_set = set()
        # for i in nums:
        #     if i in num_set:
        #         return True
        #     else:
        #         num_set.add(i)
        # return False
         