def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=2
if n<=0:
   print("please enter a positive integer")
else:
   print("fibonacci series:")
   for i in range(n):
       print(fibonacci(i))








