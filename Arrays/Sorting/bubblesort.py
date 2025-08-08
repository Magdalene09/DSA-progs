import array as ar
arr=ar.array('i',[])
a=int(input("enter ele num"))
for i in range(a):
    b=int(input("ele"))
    arr.append(b)
print(arr)


for i in range(0,len(arr)-1):  #using for loop
    for j in range(0,len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)



while True:#using while loop
    z=True
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            z=False
    if z==True:
        break
print(arr)

