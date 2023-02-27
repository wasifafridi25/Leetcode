class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0    
        a = 0
        b = 1
        c = 0
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return c 
def main():
    s1 = Solution()
    n = int(input("Enter the value of n for which you wish to see the fibonacci number: "))
    number = s1.fib(n)
    print("The Fibonnaci number is: ",number)


if __name__ == "__main__":
    main()    
    