import array as ar
arr=ar.array('i',[])
a=int(input("enter ele num"))
for i in range(a):
    b=int(input("ele"))
    arr.append(b)
print(arr)

for i in range(1,len(arr)):
    cur=arr[i]
    j=i-1
    while j>=0 and cur<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=cur

print(arr)
