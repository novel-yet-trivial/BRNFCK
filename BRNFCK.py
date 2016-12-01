pointer     = 0         # Pointer
ar          = [0]*3000  # Array
total_out   = ""        # Final output

print("Initialised Array: {} cells".format(len(ar)))

def execute(char):
    global pointer, ar, total_out
    if char == ">":
        if pointer < 3000: pointer += 1
        else: raise Exception("ERROR: Pointer cannot increase past 3000")
    elif char == "<":
        if pointer > 0: pointer -= 1
        else: raise Exception("ERROR: Pointer cannot decrease past 0")
    elif char == "+":
        if ar[pointer] < 255: ar[pointer] += 1
        else: ar[pointer] = 0
    elif char == "-":
        if ar[pointer] > 0: ar[pointer] -= 1
        else: ar[pointer] = 255
    elif char == ".":
        try:
            print("Array Value: {}".format(str(ar[pointer])))  # Array value
            print("Output:      {}".format(chr(ar[pointer])))  # chr() of value
            total_out += chr(ar[pointer])  # Append chr() to final output string
        except:
            print(". read but {} has no ASCII value".format(str(ar[pointer])))
    elif char == ",":
        inp = ord(input("INPUT: "))
        ar[pointer] = inp
    else: pass
    # Displays the character read and the first 10 values in the array/tape
    print("READ: Char: {}, Array: {}".format(char, ar[:10]))

def find_brackets(code):
    # Maps [ to ] so if a [ is encountered its corresponding ] can be found
    open_brcks = []  # Where open brackets are
    loop_map   = {}  # Maps like { pos of [ : pos of ] }
    for pos, char in enumerate(code):
        if char == "[":
            open_brcks.append(pos)  # Add to the [ list
        if char == "]":
            try:
# Remove the latest position of a [ from the list and map it to it's closing ]
                loop_map[open_brcks.pop()] = pos
            except IndexError:  # If it can't pop() beacuse there isn't a [
                raise ValueError("Too many ]'s")
    if open_brcks != []:  # If there are unmapped [
        raise ValueError("Too many ['s")
    else:
        return loop_map  # Should look like {3:8} for +++[>+<-]

def interpret(code):
    loop_map = find_brackets(code)  # Map [ to ]
    counter  = 0   # Where it is executing from
    ls_pos   = []  # List of positions of [
    while counter < len(code):
        to_exec = code[counter]  # Get the current character
        if to_exec in ["<", ">", ",", ".", "+", "-"]:
            execute(to_exec)  # Execute command
        elif to_exec == "[":
            if ar[pointer] > 0:  # If the byte at the pointer is > 0
                ls_pos.append(counter)  # Add the position to a list
            else:
                counter = loop_map[counter]  # Else skip the loop
        elif to_exec == "]":
            counter = ls_pos.pop() - 1  # Go back to the [
                                        # -1 because of the += below
        counter += 1

with open ("torture_test.bf", "r") as f:
    interpret(f.read())  # Read code from file into function

print("************\nEND RESULTS:")
print(ar[:10])  # Show first 10 in array
print("Total output: {}".format(total_out))  # Show final output
