import sys
import time   
sys.setrecursionlimit(10**5)

def Fibonacci_Recursive(n):
    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return Fibonacci_Recursive(n-1)+Fibonacci_Recursive(n-2)

def fibonacci_iterative(n):
   a = 0
   b = 1
   if n < 0:
       print("Incorrect input")
   elif n == 0:
       print(a) 
   elif n == 1:
       print(a,b)
   else:
       print(a, b, end=' ')
       for i in range(2,n+1):
           c = a + b
           a = b
           b = c
           print(c, end=' ')
def main():
    print("Fibonacci numbers after 20 cycles: ")
    start_fib_rec = time.time()
    fib_rec = Fibonacci_Recursive(20)
    end_fib_rec = time.time() - start_fib_rec
    
    start_fib_iter = time.time()
    fibonacci_iterative(20)
    end_fib_iter = time.time() - start_fib_iter
    
    print("\nHere's the execution time result for both the recursive and iterative methods: ")
    print("Recursive execution time: ", end_fib_rec)
    print("Iterative execution time: ", end_fib_iter)
    
    print("Fibonacci numbers after 42 cycles: ")
    start_fib_rec = time.time()
    fib_rec = Fibonacci_Recursive(42)
    end_fib_rec = time.time() - start_fib_rec
    
    start_fib_iter = time.time()
    fibonacci_iterative(42)
    end_fib_iter = time.time() - start_fib_iter
    
    print("\nHere's the execution time result for both the recursive and iterative methods: ")
    print("Recursive execution time: ", end_fib_rec)
    print("Iterative execution time: ", end_fib_iter)
    
    
    
    
    
if __name__ == "__main__":
    main()
                       
