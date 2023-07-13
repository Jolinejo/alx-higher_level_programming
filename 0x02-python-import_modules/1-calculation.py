#!/usr/bin/python3
def main():
    a = 10
    b = 5
    import calculator_1 as calc
    print("{a} + {b} = {val}".format(a=a, b=b, val=calc.add(a, b)))
    print("{a} - {b} = {val}".format(a=a, b=b, val=calc.sub(a, b)))
    print("{a} * {b} = {val}".format(a=a, b=b, val=calc.mul(a, b)))
    print("{a} / {b} = {val}".format(a=a, b=b, val=calc.div(a, b)))
if __name__ == "__main__":
    main()
