pointer     = 0         # Pointer
ar          = [0]*3000  # Array
total_out   = ""        # Final output
opening_brck = []       # list to contain the positions of the opening brackets

print("Initialised Array: {} cells".format(len(ar)))

def execute(char):
    global pointer, ar, total_out, opening_brck
    if char == ">":
        if pointer < 3000:
            pointer += 1
        else:
            raise Exception("ERROR: Pointer cannot increase past 3000")
    elif char == "<":
        if pointer > 0:
            pointer -= 1
        else:
            raise Exception("ERROR: Pointer cannot decrease past 0")
    elif char == "+":
        if ar[pointer] < 255:
            ar[pointer] += 1
        else:
            ar[pointer] = 0
    elif char == "-":
        if ar[pointer] > 0:
            ar[pointer] -= 1
        else:
            ar[pointer] = 255
    elif char == ".":
        try:
            print("Array Value: {}".format(str(ar[pointer])))
            print("Output:      {}".format(chr(ar[pointer])))
            total_out += chr(ar[pointer])
        except:
            print(". read but {} has no ASCII value".format(str(ar[pointer])))
    elif char == ",":
        inp = int(input("INPUT: "))
        ar[pointer] = inp
    else:
        pass
    print("READ: Char: {}, Array: {}".format(char, ar[:10]))

def interpret(code):
    for pos, char in enumerate(code):
        if char == "[":
            opening_brck.append(pos+1)  # Add 1 so it doesent execute() the
                                        # the actual [ bracket
        elif char == "]":
            try:
                loop = []  # list which maps the positions of open brackets to closed
                           # brackets
                loop.append(opening_brck.pop())  # Append to loop where the
                                                 # latest [ was and remove it
                                                 # from opening_brck so it wont
                                                 # be executed again
                loop.append(pos)  # Append pos of the latest ] bracket
                while ar[pointer] > 0:
                # execute loop
                # Below logic: execute the code after the latest [ and before
                # the latest ]
                    for x in code[loop[0]:loop[1]]:
                        execute(x)
            except IndexError:
                raise ValueError("Supplied string isn't balanced, too many ]'s!")
        else:
            execute(char)

with open ("brain.txt", "r") as f:
    interpret(f.read())  # Read code from .txt file into function

print("************\nEND RESULTS:")
print(ar[:10])  # Show first 10 in array
print("Total output: {}".format(total_out))
