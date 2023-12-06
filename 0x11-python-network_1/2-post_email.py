#!/usr/bin/python3
"""module to fetch URL"""

if __name__ == "__main__":
    from urllib import request, parse
    import sys
    email = sys.argv[2]
    data = {}
    data["email"] = email
    data = parse.urlencode(data).encode("utf-8")
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
