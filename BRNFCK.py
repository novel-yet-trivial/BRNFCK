

class PointerBoundsError(Exception):
    pass

class BrainFuck(object):
    def __init__(self):
        self.pointer = None
        self.ar = None
        self.total_out = None

    @property
    def current(self):
        return self.ar[self.pointer]

    @current.setter
    def current(self, value):
        self.ar[self.pointer] = value

    def increment_pointer(self, amount):
        self.pointer += amount
        if self.pointer > 3000:
            raise PointerBoundsError("pointer cannot increase past 3000")
        if self.pointer < 0:
            raise PointerBoundsError("pointer cannot decrease past 0")

    def increment_array(self, amount):
        self.current = (self.current + amount) % 256

    def output(self):
        try:
            char = chr(self.current)
            # Array value
            print("Array Value: {}".format(self.current))
            # chr() of value
            print("Output:      {}".format(char))
            # Append chr() to final output string
            self.total_out += char
        except ValueError:
            print(". read but {} has no ASCII value".format(self.current))

    def execute(self, char):
        if char == ">":
            self.increment_pointer(1)
        elif char == "<":
            self.increment_pointer(-1)

        elif char == "+":
            self.increment_array(1)
        elif char == "-":
            self.increment_array(-1)

        elif char == ".":
            self.output()

        elif char == ",":
            inp = ord(input("INPUT: "))
            self.ar[self.pointer] = inp

        # Displays the character read and the first 10 values in the array/tape
        print("READ: Char: {}, Array: {}".format(char,self.ar[:10]))

    def map_loops(self, code):
        # Maps [ to ] so if a [ is encountered its corresponding ] can be found
        open_brcks = []  # Where [ are
        self.loop_map   = {}  # Dict for mapping: { pos of [ : pos of ] }
        for pos, char in enumerate(code):  # Map each [ to ]
            if char == "[":
                open_brcks.append(pos)  # Add to the [ list
            if char == "]":
                try:
                # Remove the latest position of a [ from the list and map it to
                # it's closing ]
                    self.loop_map[open_brcks.pop()] = pos
                except IndexError:  # If it can't pop() beacuse there isn't a [
                    raise ValueError("Too many ]'s")
        if open_brcks:  # If there are unmapped [
            raise ValueError("Too many ['s")

    def interpret(self, code):
        self.pointer     = 0         # Pointer
        self.ar          = [0]*3000  # Array
        self.total_out   = ""        # Final output
        print("Initialised array: {} cells".format(len(self.ar)))
        self.map_loops(code)
        # Start main computations
        counter  = 0   # Where it is executing from
        open_brcks = []
        while counter < len(code):
            to_exec = code[counter]  # Get the current character
            if to_exec in {"<", ">", ",", ".", "+", "-"}:
                self.execute(to_exec)  # Execute command
            elif to_exec == "[":
                # If the byte at the self.pointer is > 0
                if self.current > 0:
                    open_brcks.append(counter)  # Add the position to a list
                else:
                    counter = self.loop_map[counter]  # Else skip the loop
            elif to_exec == "]":
                counter = open_brcks.pop() - 1  # Go back to the [
                                        # -1 because of the += below
            counter += 1
        return("************\nEND RESULTS:\n{}\nTotal output: {}".format(
                                                                self.ar[:10],
                                                                self.total_out))


def main():
    #test case
    bf = BrainFuck()
    print(bf.interpret(" -[------->+<]>++.-[--->+<]>---.")) #should print "Kk"

if __name__ == '__main__':
    main()
