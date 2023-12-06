#!/usr/bin/python3
"""module to fetch URL"""

if __name__ == "__main__":
    import requests
    import sys
    email = sys.argv[2]
    data = {}
    data["email"] = email
    r = requests.post(sys.argv[1], data)
    print(r.text)
