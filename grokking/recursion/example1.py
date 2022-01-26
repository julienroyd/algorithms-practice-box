# Visualising the stack

import traceback

def print_stack():
    print('\n\n----------------------------')
    for line in traceback.format_stack():
        print(line.strip())
    print('----------------------------')

def print_backward(x):
    print_stack()
    if x == 0:
        print(f"Reached x={x}")
    else:
        print(f"Printing x={x}")
        print_backward(x - 1)
        print(f"Ended with call x={x}")

if __name__ == '__main__':
    print_backward(3)
