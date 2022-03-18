#!/usr/bin/env python
# coding: utf-8

# read adjacent list
adjacentList = {}
f = open("C:\\Users\\Owner\\Desktop\\adjacentList.txt", "r")
cnt = 1
for l in f:
    if cnt % 2 == 1:
        target = int(l) 
    else:
        neis = l.rstrip("\n").split(",")
        neighbors = []
        for i in range(len(neis)-1):
            neighbors.append(int(neis[i]))
        adjacentList[target] = neighbors
    cnt += 1
f.close()


print(adjacentList)


# read attribute list
attributeList = {}

f = open("C:\\Users\\Owner\\Desktop\\attributeList.txt", "r")
cnt = 1
nex = True
for l in f:
    if l == "_\n":
        attributeList[target] = edges
        nex = True
        continue
    
    if nex:
        target = int(l.rstrip("\n"))
        nex = False
        edge_attr = [] # edge_attr = [length, category]
        edges = []     # edges = [[length, category], [length, category],....]
        cnt = 1
        continue
    else:
        if cnt % 2 == 1:
            edge_attr.append(float(l.rstrip("\n"))) # length is appended
            cnt += 1
        elif cnt % 2 == 0:
            edge_attr.append(l.rstrip("\n")) # category is appended
            edges.append(edge_attr)
            edge_attr = []
            cnt += 1
f.close()


print(attributeList)


# read coordinations #
coordinations = []
f = open("C:\\Users\\Owner\\Desktop\\coordinations.txt", "r")
cnt = 1
coordination = []
for l in f:
    if cnt % 3 == 0:
        coordinations.append(coordination)
        coordination = []
    else:
        coordination.append(float(l.rstrip("\n")))
    cnt += 1
f.close()


print(coordinations)