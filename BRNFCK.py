# < | ✓
# + | ✓
# > | ✓
# - | ✓
# . | ✓
# , | ✓
# [ | x
# ] | x

pointer   = 0
ar        = []
total_out = ""
for x in range (3000):
    ar.append(0)
print("Array: {}".format(len(ar)))

def execute(pos, char):
    global pointer, ar, total_out
    print(pos, char)
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
        print("Array Value: {}".format(str(ar[pointer])))
        print("Output:      {}".format(chr(ar[pointer])))
        total_out += chr(ar[pointer])
    elif char == ",":
        inp = int(input("INPUT: "))
        ar[pointer] = inp

    # How to do loop algorithm???
    elif char == "[":
        pass
    elif char == "]":
        pass
    # END loop algorithm

    else:
        pass


with open ("brain.txt", "r") as f:
    for x, y in enumerate(f.read()):
        execute(x, y)

print(ar[0:10])  # Show first 10 in array
print("Total output: {}".format(total_out))
