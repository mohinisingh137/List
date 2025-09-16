A=list(map(int,input().split()))
B=int(input())
result=[]
for num in range(len(A)):
   new_num= A[num]+B
   result.append(new_num)
print(result)