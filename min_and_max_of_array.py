
arr=list(map(int,input().split()))
max=arr[0]
min=arr[0]
for i in range(0,len(arr)):
    if arr[i]> max:
        max=arr[i]
    if arr[i]<min:
        min=arr[i]
print(max)
print(min)
