num=int(input("enter the any number"))
sum=0
x=num
while num>0:
    i=(num%10)
    a=i**3
    sum=sum+a
    num=num//10
if sum==x:
   print("it is armstrong number")
else:
    print("not armstrong number")
