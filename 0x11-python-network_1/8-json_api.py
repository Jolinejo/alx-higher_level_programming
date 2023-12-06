#!/usr/bin/python3
"""module to fetch URL"""

if __name__ == "__main__":
    import requests
    import sys
    data = {}
    try:
        data['q'] = sys.argv[1]
    except Exception:
        data['q'] = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        dictti = r.json()
        if len(dictti) != 0:
            print("[{}] {}".format(dictti["id"], dictti["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
