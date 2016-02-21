memory = {}
inv_memory = {}

import fileinput

def process_line(line):
    global memory, inv_memory
    line = line.split()
    command = line[0]

    if command == "calc":
        try:
            cur = memory[line[1]]
            index = 2
            sub_op = False
            while index < len(line) - 1:
                if line[index] == "+":
                    sub_op = False
                elif line[index] == "-":
                    sub_op = True
                else:
                    assert index % 2
                    rhs = memory[line[index]]
                    if sub_op:
                        cur -= rhs
                    else:
                        cur += rhs
                index += 1

            r = inv_memory.get(cur, "unknown")
        except KeyError:
            r = "unknown"
        print " ".join(line[1:]) + " " + r
    elif command == "def":
        if line[1] in memory:
            # Clear out the old value
            inv_memory[memory[line[1]]] = "unknown"
        memory[line[1]] = int(line[2])
        inv_memory[memory[line[1]]] = line[1]
    elif command == "clear":
        memory = {}
        inv_memory = {}

for line in fileinput.input():
    process_line(line)
