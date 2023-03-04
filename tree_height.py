# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    heights = [0] * n
    max_height = 0
    queue = []
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            heights[i] = 1
            queue.append(i)
    while queue:
        nod = queue.pop(0)
        height = heights[nod]
        for i in range(n):
            if parents[i] == nod:
                heights[i] = height + 1
                queue.append(i)
                if height + 1 > max_height:
                     max_height = heights[i]
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
    return


if __name__ == '__main__': 
    sys.setrecursionlimit(10**7)  
    threading.stack_size(2**27)  
    threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))