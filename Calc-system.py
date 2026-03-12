### --- Calc-system / calculatrice only with sys --- ###

import sys

prog_name = sys.argv.pop(0)

if len(sys.argv) < 3:
    print("error: not enough arguments")
    print(f"usage: {prog_name} OPERATION NUMBER...")
    exit(1)

operation = sys.argv.pop(0)

if operation not in ["+", "-", "x"]:
    print(f"error: wrong operation {operation}")
    print(f"usage: {prog_name} OPERATION NUMBER...")
    exit(1)

numbers = []

for arg in sys.argv:
    try:
        numbers.append(float(arg))
    except ValueError:
        print(f"error: {arg} is not a number")
        print(f"usage: {prog_name} OPERATION NUMBER...")
        exit(1)

total = numbers[0]
for number in numbers[1:]:
    if operation == "+":
        total = total + number

    if operation == "-":
        total = total - number

    if operation == "x":
        total = total * number

print(total)