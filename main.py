class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1 #Intialize left = BUY and right = SELL pointers
        maxProfit = 0
        
        while right < len(prices): #Iterate through the length of the prices list 
            #checking if pointers are giving a profitable outcome
            if prices[left] < prices[right]: 
                profit = prices[right] - prices[left] #calcualting profit
                maxProfit = max(maxProfit, profit) #New max profit is between previous max profit and newly assigned profit value 
            else:
                left = right
            right += 1
        return maxProfit
