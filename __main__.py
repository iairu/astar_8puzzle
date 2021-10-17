from _state import *


# later will be user input
n = 3 # 8-puzzle side length
init = State([3,2,8,4,5,6,7,1,0]) # initial state, 0 => empty field
init_impostor = State([3,2,8,4,5,6,7,1,0])
init_then_down = State([3,2,8,4,5,0,7,1,6])
init_then_down_again = State([3,2,8,4,5,0,7,1,6])
fin = State([1,2,3,4,5,6,7,8,0]) # final state

# existing states that if reached again won't be considered by the algorithm
# no need to include the final state, because once it will be reached the algorithm will end successfuly
states = set() 
states.add(init) # todo move this addition after the state has been expanded with operators into a tree
print(f"This should say true: {init_impostor in states}")
print(f"This should say false: {init_then_down in states}")
print(f"This should also say false: {init_then_down_again in states}")
states.add(init_then_down) # todo move this addition after the state has been expanded with operators into a tree
print(f"This should now say true: {init_then_down in states}")
print(f"This should now also say true: {init_then_down_again in states}")
print(f"There should be two states in the set: {len(states)}")
states.add(fin) 
states.add(fin) 
states.add(fin) 
states.add(fin) 
print(f"Now I tried to add the same state a number of times, but it should only be once in the set, meaning {len(states)} has to be three")

# number pair check (if there is a lone number in one of the user input states then they can't be accepted)
assert (len(init) == len(fin)), "Initial and final states must have the same element count"
for i in init.elms:
    found = False
    for j in fin.elms:
        if (i == j): 
            found = True
            break
    assert (found == True), f"An element '{i}' is missing from the final state."
