from array import array


# later will be user input
n = 3 # 8-puzzle side length
init = array("i",[3,2,8,4,5,6,7,1,0]) # initial state, 0 => empty field
fin = array("i",[1,2,3,4,5,6,7,8,0]) # final state

# states = set() # existing states that if reached again won't be considered by the algorithm
# states.add(init) # todo custom class for states first because unhashable

# number pair check (if there is a lone number in one of the user input states then they can't be accepted)
assert (len(init) == len(fin)), "Initial and final states must have the same element count"
for i in init:
    found = False
    for j in fin:
        if (i == j): 
            found = True
            break
    assert (found == True), f"An element '{i}' is missing from the final state."
