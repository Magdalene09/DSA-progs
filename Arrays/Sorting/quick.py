import array as ap #using randomized algorithm
import random
arr=ap.array('i',[])
n=int(input("enter"))
for i in range(n):
    a=int(input("enter num"))
    arr.append(a)

print(arr)

def qsort(array):
    if len(array)<=1:
        return array
    pivot=random.choice(array)

    left=[i for i in array if i<pivot]
    right=[i for i in array if i>pivot]
    middle=[i for i in array if i==pivot]

    return qsort(left)+middle+qsort(right)

sortedarr=qsort(arr.tolist())
print(sortedarr)
