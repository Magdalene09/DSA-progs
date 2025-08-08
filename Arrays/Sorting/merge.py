import array as ap
arr=ap.array('i',[])
n=int(input("enter"))
for i in range(n):
    a=int(input("enter num"))
    arr.append(a)

print(arr)

def msort(array):#split
    if len(array)>1:
        mid=len(array)//2
        left=array[:mid]
        right=array[mid:]

        msort(left)
        msort(right)

        lp=0
        rp=0
        np=0

        while (lp<len(left) and rp<len(right)):#sorting and adding
            if left[lp]<right[rp]:
                array[np]=left[lp]
                lp+=1
            else:
                array[np]=right[rp]
                rp+=1

            np+=1

        while lp<len(left):#adding remaining elements
            array[np]=left[lp]
            np+=1
            lp+=1

        while rp<len(right):
            array[np]=right[rp]
            np+=1
            rp+=1

    return array

