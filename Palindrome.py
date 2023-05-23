n=int(input())
r=0
temp=n
while n>0:
    rem=n%10
    r=r*10+rem
    n//=10
if temp==r:
    print("True")
else:
    print("False")