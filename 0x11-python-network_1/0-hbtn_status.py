#!/usr/bin/python3
"""module to fetch URL"""

if __name__ == "__main__":
    import urllib.requesit
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        html = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
