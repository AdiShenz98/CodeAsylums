def check(x,n):
    if(x%n==0):
         print("Yes")
    else:
        print("No")

t=int(input("Enter of number of test cases : "))
#a=[]
sum=0
for i in range(t):
    n=int(input("Enter the number of elements :"))
    for j in range(n):
        z=int(input("Enter value : "))
        #a.append(z)
        sum=sum+z
    check(sum,n)
