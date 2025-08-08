import array as ar
arr=ar.array('i',[])
a=int(input("enter ele num"))
for i in range(a):
    b=int(input("ele"))
    arr.append(b)
print(arr)

for first in range(len(arr)-1):
    mini=first
    for sec in range(first+1,len(arr)):
        if arr[sec]<arr[mini]:
            mini=sec
    arr[mini],arr[first]=arr[first],arr[mini]

print(arr)



