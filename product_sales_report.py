n=int(input())
sales=list(map(int,input().split()))
max=sales[0]
min=sales[0]
for i in range(0,len(sales)):
    if sales[i]> max:
        max=sales[i]
    if sales[i]<min:
        min=sales[i]
print(max , min)

