
def read_word(inputs, prompt):
    if(len(inputs) == 0):
        input_str = input(prompt)
        # modify inputs in place so changes are reflected in the caller
        inputs.clear()
        inputs.extend(input_str.split(' '))
    return inputs.popleft()
