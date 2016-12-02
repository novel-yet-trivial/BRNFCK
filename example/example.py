import sys
sys.path.append('..') #stupid hacky way to get arond package importing

from BRNFCK import BrainFuck

bf = BrainFuck(True)

with open ("torture_test.bf", "r") as f:
    print(bf.interpret(f.read()))  # Read code from file into function

