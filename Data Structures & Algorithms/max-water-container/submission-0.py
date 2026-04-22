class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1   # bug 1: was missing the 0,
        while l < r:
            area = (r - l) * min(heights[l], heights[r])  # bug 2: area= was missing, used () not []
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res



