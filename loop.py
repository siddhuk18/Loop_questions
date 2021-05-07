i=0
while True:
    print(i)
    i=i+1

guessing=30
chances=5
i=1
while i<=chances:
    num=int(input("enter the number"))
    if num==guessing:
        print("your winnar")
        break
    else:
        print("try again")
    i+=1
