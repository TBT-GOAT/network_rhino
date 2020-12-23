# coding utf-8

import rhinoscriptsyntax as rs

import math
import random
import sys
import os

edges = rs.GetObjects("select objects")

adjacentList = {}
attributeList = {}
coordinations = []
coordinations_rounded = []  # for checking if a point is searched already or not
"""
example
adjacentList =  {0: [1, 2, 3], 1: [0, 2],...}
attributeList = {0: [2.0, 5.0, 8.6], 1: [2.0, 4.7], ...}
coordinations = [[4.5, 8.2, 0.0], [5.2, 3.6, 0.0], ...]
"""

cnt = 0  # point id
for i in range(len(edges)):
    edge = edges[i]
    try:
        end_points = rs.CurvePoints(edge)
    except:
        rs.ObjectColor(edge, (255, 0, 0))
        print("Error", edge)
        break

    l = rs.CurveLength(edge)
    kind = rs.ObjectLayer(edge)

    for p in end_points:
        p_rounded = [round(p[0], 2), round(p[1], 2), round(p[2], 2)]  # round to the second decimal place
        if p_rounded in coordinations_rounded:  # this point is already searched
            pass
        else:  # search a new point
            coordinations.append(p)
            coordinations_rounded.append(p_rounded)
            adjacentList[cnt] = []
            attributeList[cnt] = []
            cnt += 1

    # two end points are connected
    point_ids = [coordinations_rounded.index([round(p[0], 2), round(p[1], 2), round(p[2], 2)]) for p in end_points]

    adjacentList[point_ids[0]].append(point_ids[1])
    adjacentList[point_ids[1]].append(point_ids[0])

    attributeList[point_ids[0]].append((l, kind))  # you can add another info in attributeList
    attributeList[point_ids[1]].append((l, kind))

for k in adjacentList.keys():
    rs.AddTextDot(k, coordinations[k])

f = open("C:\\Users\\Owner\\Desktop\\adjacentList.txt", "w")
for k, v in adjacentList.items():
    print(k, v)
    f.write(str(k) + "\n")
    for nei in v:
        f.write(str(nei) + ",")
    f.write("\n")
f.close()

f = open("C:\\Users\\Owner\\Desktop\\attributeList.txt", "w")
for k, v in attributeList.items():
    print(k, v)
    f.write(str(k) + "\n")
    for ats in v:  # ats = (length, layer_name)
        for at in ats:
            f.write(str(at) + "\n")
    f.write("_\n")
f.close()

f = open("C:\\Users\\Owner\\Desktop\\coordinations.txt", "w")
for p in coordinations:
    for u in p:
        f.write(str(u) + "\n")
f.close()