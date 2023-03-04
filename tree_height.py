# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    tree = [[]for i in range (n)]
    root = -1
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    height = 0
    queue = [root]

    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            for child in tree[node]:
                queue.append(child)
        height += 1    

    return height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
    return


if __name__ == '__main__': 
    sys.setrecursionlimit(10**7)  
    main()
