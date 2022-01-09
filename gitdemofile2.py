def rot(arr,n,d):
    ar=[]
    for i in range(n):
        count=0
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                count=count+1
        if count==0:
            ar.append(arr[i])
    print(ar)
    for i in range(d):
        rotres(ar,len(ar))
    return ar
def rotres(ar,n):
    tem=ar[0]
    for j in range(n-1):
        ar[j]=ar[j+1]
    ar[n-1]=tem
    return ar
n=int(input())
arr=list(map(int,input().split()))
d=int(input())
res=rot(arr,len(arr),d)
for i in res:
    print(i,end=" ")
