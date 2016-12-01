from BRNFCK import brainfuck

bf = brainfuck()

with open ("torture_test.bf", "r") as f:
    print(bf.interpret(f.read()))  # Read code from file into function
