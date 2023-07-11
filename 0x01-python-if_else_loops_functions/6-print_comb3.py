#!/usr/bin/python3
for num in range(0, 9):
    for second in range(num+1, 10):
        if num != 8 or second != 9:
            print("{fir}{sec}, ".format(fir=num, sec=second), end='')
print("89")
