#!/usr/bin/python3
def main():
    import calculator_1 as calc
    import sys
    n = len(sys.argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if not sys.argv[2] in "+*-/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if sys.argv[2] == '+':
        print("{a} {op} {b} = {re}".format(a=a, b=b, op=op, re=calc.add(a, b)))
    elif sys.argv[2] == '-':
        print("{a} {op} {b} = {re}".format(a=a, b=b, op=op, re=calc.sub(a, b)))
    elif sys.argv[2] == '*':
        print("{a} {op} {b} = {re}".format(a=a, b=b, op=op, re=calc.mul(a, b)))
    if sys.argv[2] == '/':
        print("{a} {op} {b} = {re}".format(a=a, b=b, op=op, re=calc.div(a, b)))


if __name__ == "__main__":
    main()
