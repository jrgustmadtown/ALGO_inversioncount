import sys
import heapq

inputy = sys.stdin.read().splitlines()
k = int(inputy[0])
index = 1
outputy = []

def IC(size, unsorted):


for _ in range(k):
    j = int(inputy[index])
    index+=1
    unsorted = list(map(int, inputy[index].split()))
    index+=1
    count = IC(j,unsorted)
    outputy.append(count)

for _ in outputy:
    print(_)
    



