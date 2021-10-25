from _state import *
from _alg import *

import time
import csv

all_n3 = []

for i in range(0,100): # run tests 100 times (around 9min)

    print("################ " + str(i + 1))
    print("N = 3 - Testing different recursion limits and difficulty - Reversed init/fin")
    print("################")

    n3 = []

    print("[#1.1]: Default recursion limit of 1000:")
    start = time.perf_counter()
    AStar.explore(State(3,[1,2,3,4,5,6,7,8,0]), State(3,[3,2,8,4,5,6,7,1,0]))
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#1.2]: Custom recursion limit of 500:")
    start = time.perf_counter()
    AStar.explore(State(3,[1,2,3,4,5,6,7,8,0]), State(3,[3,2,8,4,5,6,7,1,0]), 500)
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#1.3.1]: Custom recursion limit of 200:")
    start = time.perf_counter()
    AStar.explore(State(3,[1,2,3,4,5,6,7,8,0]), State(3,[3,2,8,4,5,6,7,1,0]), 200)
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#1.3.2]: Custom recursion limit of 200, no print:")
    start = time.perf_counter()
    AStar.explore(State(3,[1,2,3,4,5,6,7,8,0]), State(3,[3,2,8,4,5,6,7,1,0]), 200, 0)
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#1.4.1]: Custom recursion limit of 50:")
    start = time.perf_counter()
    AStar.explore(State(3,[1,2,3,4,5,6,7,8,0]), State(3,[3,2,8,4,5,6,7,1,0]), 50)
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#1.4.2]: Custom recursion limit of 50, no print:")
    start = time.perf_counter()
    AStar.explore(State(3,[1,2,3,4,5,6,7,8,0]), State(3,[3,2,8,4,5,6,7,1,0]), 50, 0)
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#2]: Default recursion limit of 1000:")
    start = time.perf_counter()
    AStar.explore(State(3,[1,2,3,4,5,6,7,8,0]), State(3,[5,0,8,4,2,1,7,3,6]))
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    print("[#3]: Default recursion limit of 1000:")
    start = time.perf_counter()
    AStar.explore(State(3,[1,2,3,4,5,6,7,8,0]), State(3,[1,2,0,4,5,3,7,8,6]))
    totalraw = time.perf_counter() - start
    total = str(round(totalraw,6))
    n3.append(total)
    print("Took " + total + "sec \n---")

    all_n3.append(n3.copy())

with open("tester_n3_reverse.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    writer.writerows(all_n3)