# Devin Benninghoven

inputStrings = [
    "(id+id)*id$",
    "id*id$",
    "(id*)$",
]

productionRules = {
    1: ('E', ['E', '+', 'T']),
    2: ('E', ['T']),
    3: ('T', ['T', '*', 'F']),
    4: ('T', ['F']),
    5: ('F', ['(', 'E', ')']),
    6: ('F', ['id']),
}

parsingTable = {
    0:  {"id": "S5", "+": None, "*": None, "(": "S4", ")": None, "$": None, "E": 1, "T": 2, "F": 3},
    1:  {"id": None, "+": "S6", "*": None, "(": None, ")": None, "$": "acc", "E": None, "T": None, "F": None},
    2:  {"id": None, "+": "R2", "*": "S7", "(": None, ")": "R2", "$": "R2", "E": None, "T": None, "F": None},
    3:  {"id": None, "+": "R4", "*": "R4", "(": None, ")": "R4", "$": "R4", "E": None, "T": None, "F": None},
    4:  {"id": "S5", "+": None, "*": None, "(": "S4", ")": None, "$": None, "E": 8, "T": 2, "F": 3},
    5:  {"id": None, "+": "R6", "*": "R6", "(": None, ")": "R6", "$": "R6", "E": None, "T": None, "F": None},
    6:  {"id": "S5", "+": None, "*": None, "(": "S4", ")": None, "$": None, "E": None, "T": 9, "F": 3},
    7:  {"id": "S5", "+": None, "*": None, "(": "S4", ")": None, "$": None, "E": None, "T": None, "F": 10},
    8:  {"id": None, "+": "S6", "*": None, "(": None, ")": "S11", "$": None, "E": None, "T": None, "F": None},
    9:  {"id": None, "+": "R1", "*": "S7", "(": None, ")": "R1", "$": "R1", "E": None, "T": None, "F": None},
    10: {"id": None, "+": "R3", "*": "R3", "(": None, ")": "R3", "$": "R3", "E": None, "T": None, "F": None},
    11: {"id": None, "+": "R5", "*": "R5", "(": None, ")": "R5", "$": "R5", "E": None, "T": None, "F": None},
    }

# STACK
# STEP STACK INPUT ACTION


def parse_input(input_string):
    stack = [0]  # Start with the initial state
    input_string += '$'  # Add end-of-input marker

    while True:
        current_state = stack[-1]
        input_symbol = input_string[0]

        action = parsingTable[current_state][input_symbol]

        if action[0] == 'S':  # Shift
            stack.append(int(action[1:]))  # Push the new state
            input_string = input_string[1:]  # Consume the input symbol
        elif action[0] == 'R':  # Reduce
            production = int(action[1:])
            for _ in range(len(productionRules[production][1])):
                stack.pop()  # Pop symbols based on the production length
            goto_state = parsingTable[stack[-1]][productionRules[production][0]]
            stack.append(goto_state)
        elif action == 'acc':  # Accept
            print("Input accepted!")
            break
        else:
            print("Input rejected!")
            break

parse_input("id*id$")
