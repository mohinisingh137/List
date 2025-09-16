A=list(map(int,input().split()))
odd=[]
even=[]
for i in range(len(A)):
    if A[i]%2 ==0:
        even.append(A[i])
    else:
        odd.append(A[i])
for num in odd:
    print(num, end=" ")
print()
for num in even:
    print(num, end=" ")
