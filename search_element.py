arr=list(map(int,input().split()))
B=int(input())
for i in range(0,len(arr)):
    if (B==arr[i]):
        print("1")
    else:
        print("0")
