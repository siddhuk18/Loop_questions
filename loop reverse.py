num=int(input("enter the number"))
sum=0
while num>0:
    m=num%10
    sum=sum*10+m
    num=num//10
print(sum)
  
