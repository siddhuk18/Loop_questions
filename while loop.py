var=int(input("enter the any number"))
rev=0
while var>0:
    digit=var%10
    rev=rev*10+digit
    var=var//10
print("reverse",rev)

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

i=1
while i<=100:
    if i%2:
        print("+",i)
        i=i+1
    print("-",i)
    i=i+1

i=0
while i<=100:
    num=i%7
    print(i)
    i=i+1

i=1
sum=0
while i<=100:
    sum=sum+i
    i=i+1
    print(sum)

num=int(input("enter the any number"))
i=1
sum=num
while i<=num:
    sum=sum+i
    i=i+1
    print(i)

num=int(input("enter the any number"))
a=5
i=1
while i<=a:
    num=int(input("enter the any number"))
    b=15
    if num<b:
        print("too low")
    if num>b:
        print("too high")
        if num==b:
            print("guessing is the correct")
        break
    else:
        print("incorrect")
    i=i+1

n=int(input("enter the number"))
i=1
while i<n:
    b=1
    while b<=i:
        print("01",end=" ")
        b=b+1
    print()
    i=i+1

gassing=30
chance=5
i=1
while i<=chance:
    num=int(input("enter the number"))
    if num==gassing:
        print(" yehh...your winner your gessing number is right..")
        break
    else:
        print("try again babu..")
    i=i+1

num=int(input("enter the any number"))
row=0
while row<num:
    space=num-row-1
    while space>0:
        print(end=" ")
        space=space-1
    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    row=row+1
    print()

a=10
i=1
s=0
while i<=a:
    num=int(input("enter your number"))
    s=s+num
    print(s)
    i+=1


i=5
while i>0:
    print(i,i,i,i,i,i)
    i=i-1

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

i=1
while i<=100:
    if i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")
    elif i%3==0:
        print("navgurukul")
    else:
        print(i)
    i=i+1