n=int(input())
emp_id=list(map(int,input().split()))
even=[]
for i in range (len(emp_id)):
    if emp_id[i]%2==0:
        even.append(emp_id[i])
    elif emp_id[i]<0:
        print(" -1")
        break
for num in even:
    print(num ,end=" ")


