a= int(input("enter a number"))
temp=a
n=0

while temp>0:
    d=temp%10
    n=n*10+d
    temp//=10
print('reverse=',n)   
