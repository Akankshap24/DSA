def fibonacci(n):
    if n == 0:  
        return 0
    if n == 1: 
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(1)) 
print(fibonacci(0)) 
print(fibonacci(7))  

