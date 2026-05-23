class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r  # Move left pointer to r (new potential minimum)
            r += 1    # r += 1 must be inside the while loop
        return maxP


            
        
        
        