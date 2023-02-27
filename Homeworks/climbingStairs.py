class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            prev1 = 1
            prev2 = 2
            current = 0    
            for i in range(2, n):
                current = prev1 + prev2
                prev1 = prev2
                prev2 = current
            return current 
        
def main():
    s = Solution()
    print("Test case 1: ")
    number = s.climbStairs(2)
    print("Number of ways to climb the stairs and reach the top: ",number )
    
    print("Test case 2: ")
    number = s.climbStairs(3)
    print("Number of ways to climb the stairs and reach the top: ",number )

if __name__ == "__main__":
    main()               
