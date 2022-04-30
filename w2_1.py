arr=[2,3,5,7,11,13,17,19]
n=int(input("Number:"))
k=0

j=1
while j <= n:
    i = arr[k]
    arr.remove(i)
    arr.append(i)
    j=j+1

    print(arr)

