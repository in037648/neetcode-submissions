class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        max_key = 0
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for key, value in d.items():
            if value > count:
                count = value
                max_key = key

        return max_key

       
        