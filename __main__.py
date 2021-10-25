from _state import *
from _alg import *
from _seq import FinSequence

# later will be user input
n = 3 # 8-puzzle side length
init = State(n,[3,2,8,4,5,6,7,1,0]) # initial state, 0 => empty field
fin = State(n,[1,2,3,4,5,6,7,8,0]) # final state

init2 = State(n,[5,0,8,4,2,1,7,3,6]) # initial state, 0 => empty field # todo later: delete, temp additional print check
fin2 = State(n,[1,2,3,4,5,6,7,8,0]) # final state # todo later: delete, temp additional print check

init3 = State(n,[1,2,0,4,5,3,7,8,6]) # initial state, 0 => empty field # todo later: delete, temp additional print check
fin3 = State(n,[1,2,3,4,5,6,7,8,0]) # final state # todo later: delete, temp additional print check

# number pair check (if there is a lone number in one of the user input states then they can't be accepted)
assert (len(init) == len(fin)), "Initial and final states must have the same element count"
init_count = 0
found_zero = False
for i in init.elms:
    init_count += 1
    found = False
    for j in fin.elms:
        if (i == j): 
            found = True
            if (i == 0):
                found_zero = True
            break
    assert (found == True), f"An element '{i}' is missing from the final state."
assert (found_zero == True), f"An element '0' (representing an empty field) must be included in both states."
# side length is not part of the state and is simply checked ahead to speed things up
assert (init_count == n * n), f"The number of elms in a state has to be n * n, otherwise it wouldn't be much of a side length, now would it?"

explored = AStar.explore(init, fin)
if isinstance(explored,FinSequence):
    explored.print()

explored = AStar.explore(init2, fin2)
if isinstance(explored,FinSequence):
    explored.print()

explored = AStar.explore(init3, fin3)
if isinstance(explored,FinSequence):
    explored.print()
