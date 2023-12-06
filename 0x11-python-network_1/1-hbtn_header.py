#!/usr/bin/python3
"""module to fetch URL"""

if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as res:
        html = res.read()
        print(res.info().get('X-Request-Id'))
