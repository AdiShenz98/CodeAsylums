def rev(x):
    rev=0
    while(x>0):
        digit=x%10
        rev=rev*10+digit
        x=x//10
    return rev



n=int(input("Enter the iteration :"))

for i in range(n):
    x=int(input("Enter value 1:"))
    y=int(input("Enter value 2:"))
    z=rev(rev(x)+rev(y))
    print(z)