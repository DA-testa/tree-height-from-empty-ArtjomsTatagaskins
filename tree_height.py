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
    mode = input("F or I: ").upper()
    while mode not in ('I', 'F'):
        mode = input("Invalid mode").upper()

    if mode == 'I':
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        file_name = input()
        path = './test/'
        file_name_full = file_name + path
        if 'a' not in file_name:
            try:
                with open (file_name_full, 'r') as file:
                    n = int(file.readline().strip())
                    parents = list(map(int, file.readline().strip().split()))
            except FileNotFoundError:
                print("File not found")
                return
        else:
            print("Can't contain letter a")

    print(compute_height(n, parents))


if __name__ == '__main__': 
    sys.setrecursionlimit(10**7)  
    main()
