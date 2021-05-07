var=int(input("enter the any number"))
rev=0
while var>0:
    digit=var%10
    rev=rev*10+digit
    var=var//10
print("reverse",rev)

