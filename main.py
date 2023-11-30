# Devin Benninghoven
# Daniel Garcia

inputStrings = [
    ["(", "id", "+", "id", ")", "*", "id", "$"],
    ["id", "*", "id", "$"],
    ["(", "id", "*", ")", "$"],
]

productionRules = {
    1: ('E', ['E', '+', 'T']),
    2: ('E', ['T']),
    3: ('T', ['T', '*', 'F']),
    4: ('T', ['F']),
    5: ('F', ['(', 'E', ')']),
    6: ('F', ['id']),
}

first = {
    "E": ["(", "id"],
    "T": ["(", "id"],
    "F": ["(", "id"],
        }

follow = {
    "E": ["+", ")", "$"],
    "T": ["+", "*", ")", "$"],
    "F": ["+", "*", ")", "$"],
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


def parse_input(inputString):

    originalInput = inputString

    stack = [0]  # Start with the initial state
    step = 0

    while True:

        step += 1

        outputLine = ""
        outputLine += str(step)
        outputLine += " "

        currentState = stack[-1]

        outputLine += str(stack)
        outputLine += " "

        inputSymbol = inputString[0]
        outputLine += str(inputSymbol)
        outputLine += " "

        action = parsingTable[currentState][inputSymbol]

        outputLine += str(action)

        print(outputLine)

        if not action:
            print(f"{originalInput} is rejected")
            break

        if action[0] == 'S':
            stack.append(int(action[1:]))
            inputString = inputString[1:]

        elif action[0] == 'R':
            production = int(action[1:])
            for _ in range(len(productionRules[production][1])):
                stack.pop()
            goto_state = parsingTable[stack[-1]][productionRules[production][0]]
            stack.append(goto_state)

        elif action == 'acc':
            print(f"{originalInput} is accepted")
            break

        else:
            print(f"{originalInput} is rejected")
            break


for inputString in inputStrings:
    parse_input(inputString)
