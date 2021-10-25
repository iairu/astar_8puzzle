from _state import *
from _alg import *
import sys

def in_sidelen():
    # Side length user input
    n = 0
    try:
        n = int(input("Enter side length of ?-puzzle (3 for 8-puzzle because 3x3=9): ")) # 8-puzzle side length
    except:
        print("Error: Invalid value, enter a number!")
        sys.exit()
    return n

def in_elms(sidelen: int, state_name: str = ""):
    # Elements
    traversed = []
    count = sidelen * sidelen

    print(state_name + " state - Input " + str(count) + " elements, use 0 for an empty one.")
    print("Use spaces for separation of elements, hit Enter when done:")

    x = input() # input() can't be limited to single char
    rawelms = x.split(" ") # space separated input

    # check every element for validity
    i = 0
    for i,e in enumerate(rawelms):
        try:
            elm = int(e)
        except:
            print("Error: Invalid value, enter numbers! Separate with spaces!")
            sys.exit()
        if (elm < 0 or elm > count - 1):
                print("Error: Invalid element (must be <0;" + str(count - 1) + ">, but found " + str(elm) + ")")
                sys.exit()
        if (i > count - 1):
                print("Error: Too many elements!")
                sys.exit()
        if (elm in traversed):
            print("Error: Duplicate input for element " + str(elm))
            sys.exit()
        traversed.append(elm)
    if (i != count - 1):
        print("Error: Not enough elements! Only entered " + str(i + 1))
        sys.exit()

    return traversed

def in_rec_depth(default_rec_depth: int):
    # Recursion depth
    try:
        rd = input("Enter recursion depth or leave empty for default (" + str(default_rec_depth) + "): ")
    except:
        print("Error: Invalid value, enter a number or nothing!")
        sys.exit()

    if (rd == ""):
        out = default_rec_depth
    else:
        out = int(rd)
        if (out < 0):
            print("Error: Invalid value, enter a number!")
            sys.exit()
    return out


# ---------------------------------

def main():

    n = in_sidelen()
    init = State(n, in_elms(n, "Initial"))
    fin = State(n, in_elms(n, "Final"))
    AStar.explore(init, fin, in_rec_depth(sys.getrecursionlimit() - 150)) # assumed ideal recursion limit, slightly below python limit which is multitudes lower than C limit

    # init1 = State(n,[3,2,8,4,5,6,7,1,0])
    # fin1 = State(n,[1,2,3,4,5,6,7,8,0])

    # init2 = State(n,[5,0,8,4,2,1,7,3,6])
    # fin2 = State(n,[1,2,3,4,5,6,7,8,0])

    # init3 = State(n,[1,2,0,4,5,3,7,8,6])
    # fin3 = State(n,[1,2,3,4,5,6,7,8,0])

    # AStar.explore(init1, fin1)
    # AStar.explore(init2, fin2)
    # AStar.explore(init3, fin3)

if __name__ == "__main__":
    main()