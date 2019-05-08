"""
Utility module for common helper functions
"""
ITEM_KEY = "todo_items" #used to store where items are stored within objects

def read_word(inputs, prompt):
    """
    reads a word from inputs or if inputs is empty, provides
    prompt to the user. Modifies inputs to hold the whitespace separated user input from prompt.
    returns what word is read
    """
    if not inputs:
        input_str = input(prompt)
        # modify inputs in place so changes are reflected in the caller
        inputs.clear()
        inputs.extend(input_str.split(' '))
    return inputs.popleft()

def read_line(inputs, prompt):
    """
    reads a line from inputs
    if they are empty, issues prompt to the user
    returns the line read
    """
    if inputs:
        name = ' '.join(inputs) # read until the end of the line
    else:
        name = input(prompt)
    inputs.clear() #consumes the rest of inputs
    return name
