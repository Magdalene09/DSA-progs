#only for sorted array two pointer algorithm is used




import array as ar
arr=ar.array('i',[])
n=int(input("enter the number of elements to be entered"))
for i in range(n):
    v=int(input("enter elements"))
    arr.append(v)

print(arr)


tar=int(input("enter the target"))
p1=0
p2=len(arr)-1
h=1
new=[]

while(p1<p2):
    act=arr[p1]+arr[p2]
    if act==tar:
        h=0
        new.append(arr[p1])
        new.append(arr[p2])       # showing output as list
        print(new)
        break
    elif act>tar:
        p2=p2-1
    elif act<tar:
        p1=p1+1


if h==1:
    print("target not found")
