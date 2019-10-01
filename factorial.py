f=1
n=int(input())
if n>0:
    for i in range(1,n+1):
         f*=i
elif n==0:
    print(1)
else:
    print("Wrong Input")
print(f)
