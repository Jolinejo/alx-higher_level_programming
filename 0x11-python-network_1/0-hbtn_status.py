#!/usr/bin/python3
"""module to fetch URL"""

import urllib.request
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    html = response.read()
    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(html.decode('utf-8')))
