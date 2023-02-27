class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r, maxProfit = 0, 1, 0
        while r < len(prices):
            if prices[r] >= prices[l]:
                curProfit = prices[r] - prices[l]
                maxProfit = max(curProfit, maxProfit)
            else:
                l = r
            r += 1
        return maxProfit

def main():
    s = Solution()
    print("Test case 1: ")
    profit1 = s.maxProfit([7,1,5,3,6,4])
    print("Max profit is: ", profit1)
    
    print("Test case 2: ")
    profit2 = s.maxProfit([7,6,4,3,1])
    print("Max profit is: ", profit2)
    
    print("Test case 3: ")
    profit3 = s.maxProfit([7,1,7,8,8,9])
    print("Max profit is: ", profit3)
    
    
    
    

if __name__ == "__main__":
    main()    