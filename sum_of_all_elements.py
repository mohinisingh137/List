arr=[1,2,3,4,5]
arr=list(map(int,input().split()))
sum=0
for i in range(0,len(arr)):
    sum=sum+arr[i]
print(sum)
