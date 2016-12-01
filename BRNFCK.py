class brainfuck():
    def __init__(self):
        self.pointer     = 0         # self.pointer
        self.ar          = [0]*3000  #self.array
        self.total_out   = ""        # Final output
        print("Initialised array: {} cells".format(len(self.ar)))

    def execute(self, char):
        if char == ">":
            if self.pointer < 3000: self.pointer += 1
            else: raise Exception("ERROR: pointer cannot increase past 3000")
        elif char == "<":
            if self.pointer > 0: self.pointer -= 1
            else: raise Exception("ERROR: pointer cannot decrease past 0")
        elif char == "+":
            if self.ar[self.pointer] < 255:self.ar[self.pointer] += 1
            else:self.ar[self.pointer] = 0
        elif char == "-":
            if self.ar[self.pointer] > 0:self.ar[self.pointer] -= 1
            else:self.ar[self.pointer] = 255
        elif char == ".":
            try:
                # Array value
                print("Array Value: {}".format(str(self.ar[self.pointer])))
                # chr() of value
                print("Output:      {}".format(chr(self.ar[self.pointer])))
                # Append chr() to final output string
                self.total_out += chr(self.ar[self.pointer])
            except:
                print(". read but {} has no ASCII value".format(
                                                    str(self.ar[self.pointer])))
        elif char == ",":
            inp = ord(input("INPUT: "))
            self.ar[self.pointer] = inp
        else: pass
        # Displays the character read and the first 10 values in the array/tape
        print("READ: Char: {}, Array: {}".format(char,self.ar[:10]))

    def interpret(self, code):
        # Maps [ to ] so if a [ is encountered its corresponding ] can be found
        open_brcks = []  # Where [ are
        loop_map   = {}  # Dict for mapping: { pos of [ : pos of ] }
        for pos, char in enumerate(code):  # Map each [ to ]
            if char == "[":
                open_brcks.append(pos)  # Add to the [ list
            if char == "]":
                try:
                # Remove the latest position of a [ from the list and map it to
                # it's closing ]
                    loop_map[open_brcks.pop()] = pos
                except IndexError:  # If it can't pop() beacuse there isn't a [
                    raise ValueError("Too many ]'s")
        if open_brcks != []:  # If there are unmapped [
            raise ValueError("Too many ['s")
        # Start main computations
        counter  = 0   # Where it is executing from
        while counter < len(code):
            to_exec = code[counter]  # Get the current character
            if to_exec in ["<", ">", ",", ".", "+", "-"]:
                self.execute(to_exec)  # Execute command
            elif to_exec == "[":
                # If the byte at the self.pointer is > 0
                if self.ar[self.pointer] > 0:
                    open_brcks.append(counter)  # Add the position to a list
                else:
                    counter = loop_map[counter]  # Else skip the loop
            elif to_exec == "]":
                counter = open_brcks.pop() - 1  # Go back to the [
                                        # -1 because of the += below
            counter += 1
        return("************\nEND RESULTS:\n{}\nTotal output: {}".format(
                                                                self.ar[:10],
                                                                self.total_out))
