#!/bin/bash
#outputcode 200
curl -s -o dev/null/ -w "%{http_code}" $1
