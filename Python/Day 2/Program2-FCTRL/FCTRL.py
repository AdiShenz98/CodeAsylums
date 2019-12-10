def noofzeroes(x):
    count=0
    for i in range(len(x)):
        while(x>0):
            if(x%10==0):
                count=count+1
                x=x//10
            else:
                break
    print(count)

def fact(x):
    factorial=0
    for i in range(1,len(x)):
        factorial=factorial*i
    return factorial

n=int(input("Enter the number of input : "))
a=[]
for i in range(n):
    z=int(input("Enter the value : "))
    a.append(fact(z))


for j in range(n):
    noofzeroes(a[j])

    