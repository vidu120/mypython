a = int(input())
elems = [int(x) for x in input().split()]
mine = ()

#the index positions for the two largest numbers.
index1= 0
index2 =0
max_1 = 0
max_2 = 0
for i in range(len(elems)):
    if max_1 < elems[i]:
        max_1 = elems[i]
        index1 = i
for i in range(len(elems)):
    if index1 != i and max_2 < elems[i]:
        max_2 = elems[i]
        index2 = i
assert(index1 != index2)
print(elems[index1] * elems[index2])
