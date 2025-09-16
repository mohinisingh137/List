A=list(map(int,input().split()))
B=[]
for i in range(len(A)):
    B.append(A[len(A)-1-i])
print(B)