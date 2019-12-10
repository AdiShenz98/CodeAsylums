mylist=[2,5,4,1,7,8,9,9,9,9]
mylist1=list(set(mylist))

max1=max(mylist1)
flag=0
for i in mylist1:
    flag=flag+1
    if(i==max1):
        flag=i
        break
mylist1.pop(flag)
print(max(mylist1))
