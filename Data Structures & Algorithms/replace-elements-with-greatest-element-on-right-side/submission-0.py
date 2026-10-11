class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0]*n
        for i in range(n):
            r = -1
            for j in range(i+1,n):
                r = max(r, arr[j])
            ans[i] = r
        return ans
