

class PointerBoundsError(Exception):
    pass

class BrainFuck(object):
    def __init__(self, debug=False):
        self.debug = debug
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
            if self.debug:
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

    def find_next_close(self, code, counter):
        '''finds the next closing bracket.
        skips the complete brackets in between'''
        while True:
            open_ = code.find('[', counter+1)
            close_ = code.find(']', counter+1)
            if 0 <= open_ < close_:
                counter = self.find_next_close(code, open_)
            else:
                return close_

    def interpret(self, code):
        self.pointer     = 0         # Pointer
        self.ar          = [0]*3000  # Array
        self.total_out   = ""        # Final output
        print("Initialised array: {} cells".format(len(self.ar)))

        # Start main computations
        counter  = 0   # Where it is executing from
        open_brcks = []
        while counter < len(code):
            to_exec = code[counter]  # Get the current character
            if to_exec == "[":
                # If the byte at the self.pointer is > 0
                if self.current:
                    open_brcks.append(counter)  # Add the position to a list
                else:
                    counter = self.find_next_close(code, counter) #find the matching bracket
            elif to_exec == "]":
                counter = open_brcks.pop() - 1  # Go back to the [
                                        # -1 because of the += below
            else:
                self.execute(to_exec)  # Execute command
            counter += 1

            if self.debug:
                # Displays the character read and the first 10 values in the array/tape
                if to_exec in "[]<>+-.,":
                    print("READ: Count: {}, Char: {}, Val: {}, Array: {}".format(counter, to_exec, self.current, self.ar[:10]))


        return("************\nEND RESULTS:\n{}\nTotal output: {}".format(
                                                                self.ar[:10],
                                                                self.total_out))

def main():
    #test case
    bf = BrainFuck()
    print(bf.interpret(" -[------->+<]>++.-[--->+<]>---.")) #should print "Kk"

if __name__ == '__main__':
    main()
