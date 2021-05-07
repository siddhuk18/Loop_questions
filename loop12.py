num=int(input("enter the number"))
i=1
sum=0
while i<num:
    if num%1==0:
        print(i)
        sum=sum+num
    i=i+1
if sum==num:
    print("prime number")
else:
    print("not prime number")
