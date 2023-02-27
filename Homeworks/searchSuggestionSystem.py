class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        res = []
        products.sort()
        l, r = 0, len(products) - 1
        for i in range(len(searchWord)):
            while l <= r and (len(products[l]) <= i or products[l][i] != searchWord[i]):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != searchWord[i]):
                r-= 1

            res.append([])
            remaining = r - l + 1
            mn = min(3, remaining)
            for i in range(mn):
                res[-1].append(products[l + i])
        
        return res

def main():
    s1 = Solution()
    p1 = ["mobile","mouse","moneypot","monitor","mousepad"]
    w1 = "mouse"
    result1 = s1.suggestedProducts(p1, w1)
    print("Example 1: ")
    print(result1)
    
    print("\nExample 2: ")
    p2 = ["havana"]
    w2 = "havana"
    result2 = s1.suggestedProducts(p2, w2)
    print(result2)
    
    

if __name__ == "__main__":
    main()    
        