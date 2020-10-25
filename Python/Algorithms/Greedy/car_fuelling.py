d=int(input())
m=int(input())
n=int(input())
x=[int(z) for z in input().split(" ")]
dist_travelled=0
i=0
refuel=0
while(dist_travelled<d and i<n-1):
    if(dist_travelled+m>=d):
        break
    if(dist_travelled+m>=x[i] and dist_travelled+m<x[i+1]):
        dist_travelled=x[i]
        refuel+=1
    elif(dist_travelled+m<x[i]):
        refuel=-1
        break
    i+=1
if(dist_travelled+m>=x[n-1] and dist_travelled+m<d):
    refuel+=1
    dist_travelled=x[n-1]

if(dist_travelled+m<d):
    refuel=-1
print(refuel)
