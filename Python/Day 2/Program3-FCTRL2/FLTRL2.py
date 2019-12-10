def factorial(x):
    factorial=1
    for i in range(1,x+1):
        factorial=factorial*i
    print(factorial)

n=int(input("Enter the number of iterations : "))

for i in range(n):
    x=int(input("Enter a value : "))
    factorial(x)