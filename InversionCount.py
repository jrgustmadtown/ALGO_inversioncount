import sys

inputy = sys.stdin.read().splitlines()
k = int(inputy[0])
index = 1
outputy = []

def MergeCount(front, back):
    S = []
    c=0
    while front or back:
        if not back:
            S.append(front.pop(0))
        elif not front:
            S.append(back.pop(0))
        else:
            if front[0] < back[0]:
                S.append(front.pop(0))
            else:
                S.append(back.pop(0))
                c+=len(front)
    return S,c

def CountSort(size, elems):
    if size <= 1:
        return 1
    mid = size // 2
    front, fc = CountSort(mid, elems[:mid])
    back, bc = CountSort(size-mid, elems[mid:])
    merged, c = MergeCount(front, back)
    return merged, c

for _ in range(k):
    j = int(inputy[index])
    index+=1
    unsorted = list(map(int, inputy[index].split()))
    index+=1
    sorted, count = CountSort(j,unsorted)
    outputy.append(count)

for _ in outputy:
    print(_)
    



