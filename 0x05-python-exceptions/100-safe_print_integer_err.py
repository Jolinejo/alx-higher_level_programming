#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        import sys
        sys.stderr.write("Exception: {}".format(str(e)))
        sys.stderr.flush()
        return False
