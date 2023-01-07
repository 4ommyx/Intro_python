# Fibonacci | 0 1 1 2 3 5 8 13...

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

x = int(input("Enter your num : "))
for i in range(x):
    print(fibo(i))  