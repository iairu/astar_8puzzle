from _state import *
from _alg import *

import time
import csv
import sys

all_n3 = []

for i in range(0,100): # run tests 100 times (around 9min)

    print("################ " + str(i + 1))
    print("N = 3 - Testing different recursion limits and difficulty")
    print("Heuristic no.1: Number of elms that aren't in final position")
    print("################")

    n3 = []

    sys.setrecursionlimit(2500)
    maxrec = sys.getrecursionlimit() - 50
    print("Maximum Python recursion set to: " + str(sys.getrecursionlimit()))
    print("Maximum Argument recursion set to: " + str(maxrec))

    print("[#1.1]: Default recursion limit of 1000:")
    start = time.perf_counter()
    AStar.explore(State(3,[3,2,8,4,5,6,7,1,0]), State(3,[1,2,3,4,5,6,7,8,0]), 1, maxrec)
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#1.2]: Custom recursion limit of 500:")
    start = time.perf_counter()
    AStar.explore(State(3,[3,2,8,4,5,6,7,1,0]), State(3,[1,2,3,4,5,6,7,8,0]), 1, 500)
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#1.3.1]: Custom recursion limit of 200:")
    start = time.perf_counter()
    AStar.explore(State(3,[3,2,8,4,5,6,7,1,0]), State(3,[1,2,3,4,5,6,7,8,0]), 1, 200)
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#1.3.2]: Custom recursion limit of 200, no print:")
    start = time.perf_counter()
    AStar.explore(State(3,[3,2,8,4,5,6,7,1,0]), State(3,[1,2,3,4,5,6,7,8,0]), 1, 200, 0)
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#1.4.1]: Custom recursion limit of 50:")
    start = time.perf_counter()
    AStar.explore(State(3,[3,2,8,4,5,6,7,1,0]), State(3,[1,2,3,4,5,6,7,8,0]), 1, 50)
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#1.4.2]: Custom recursion limit of 50, no print:")
    start = time.perf_counter()
    AStar.explore(State(3,[3,2,8,4,5,6,7,1,0]), State(3,[1,2,3,4,5,6,7,8,0]), 1, 50, 0)
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#2]: Default recursion limit of 1000:")
    start = time.perf_counter()
    AStar.explore(State(3,[5,0,8,4,2,1,7,3,6]), State(3,[1,2,3,4,5,6,7,8,0]), 1, maxrec)
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#3]: Default recursion limit of 1000:")
    start = time.perf_counter()
    AStar.explore(State(3,[1,2,0,4,5,3,7,8,6]), State(3,[1,2,3,4,5,6,7,8,0]), 1, maxrec)
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    all_n3.append(n3.copy())

with open("tester_n3_h1.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    writer.writerows(all_n3)