# Factorial 5! = 5*4*3*2*1

def factorial(n):
    if n == 1 :
        return n 
    else:
        return n * factorial(n-1)

x = factorial(12)
print(x)
