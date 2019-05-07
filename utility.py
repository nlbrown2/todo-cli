
kItemKey = "todoItems" #used to store where items are stored within objects
def read_word(inputs, prompt):
    if(len(inputs) == 0):
        input_str = input(prompt)
        # modify inputs in place so changes are reflected in the caller
        inputs.clear()
        inputs.extend(input_str.split(' '))
    return inputs.popleft()

def read_line(inputs, prompt):
    if(len(inputs) != 0):
        name = ' '.join(inputs) # read until the end of the line
    else:
        name = input(prompt)
    inputs.clear() #consumes the rest of inputs
    return name
