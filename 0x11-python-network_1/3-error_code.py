#!/usr/bin/python3
"""module to fetch URL"""

if __name__ == "__main__":
    from urllib import request, parse, error
    import sys
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except error.URLError as e:
        print("Error code: {}".format(e.code))
