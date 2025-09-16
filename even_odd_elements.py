A=list(map(int,input().split()))
even_count=0
odd_count=0
for i in range(len(A)):
    if A[i] % 2==0:
        even_count+=1
    else:
        odd_count+=1
sub=even_count-odd_count
print(sub)

