#!/bin/bash
#outputcode 200
curl -sIX OPTIONS $1 | grep -i "Allow" | cut -d' ' -f2-
