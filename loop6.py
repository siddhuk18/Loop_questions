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