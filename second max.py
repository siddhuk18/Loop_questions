num=[50,40,23,70,56,12,5,10,7]
i=0
a=num[0]
while i<len(num):
        if num[i]>a:
            a=num[i]
        i=i+1
num.remove(a)
k=0
b=num[0]
while k<len(num):
    if num[k]>b:
        a=num[k]
    k=k+1
print(a)