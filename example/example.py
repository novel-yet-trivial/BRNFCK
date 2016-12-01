import sys
sys.path.append('..')
from BRNFCK import BrainFuck

bf = BrainFuck()

with open ("torture_test.bf", "r") as f:
    print(bf.interpret(f.read()))  # Read code from file into function
