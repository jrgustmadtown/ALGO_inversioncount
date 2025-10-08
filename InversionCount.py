import sys

inputy = sys.stdin.read().splitlines()
k = int(inputy[0])
index = 1
outputy = []

def MergeCount(front, back):
    S = []
    c=0
    i,j=0,0

    while i<len(front) and j<len(back):
        if front[i] <= back[j]:
            S.append(front[i])
            i+=1
        else:
            S.append(back[j])
            j+=1
            c+=len(front)-i

    S.extend(front[i:])
    S.extend(back[j:])
    return S,c

def CountSort(size, elems):
    if size <= 1:
        return elems, 0
    mid = size // 2
    front, fc = CountSort(mid, elems[:mid])
    back, bc = CountSort(size-mid, elems[mid:])
    merged, c = MergeCount(front, back)
    return merged, c+fc+bc

for _ in range(k):
    j = int(inputy[index])
    index+=1
    unsorted = list(map(int, inputy[index].split()))
    index+=1
    sorted, count = CountSort(j,unsorted)
    outputy.append(count)

for _ in outputy:
    print(_)
    



