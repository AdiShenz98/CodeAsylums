mylist=[2,5,3,6,7,8]
count=0
flag=0
n=int(input("Enter the number to be searched : "))
for i in mylist:
    count=count+1
    if(i==n):
        print("Value found at ",count)
        flag=flag+1
if(flag==0):
    print("Value not found")
