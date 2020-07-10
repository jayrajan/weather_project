# Code written by Jerin Rajan on 09th Jul 2020

import json

# count = 0
# Parse the JSON file
fname = 'weather.json'
with open(fname) as f:
    # d = json.loads(f.read())

    for i in f:
        res = json.loads(i)
    print(res['city'])
    print(res['main'])
    print(res['wind'])
    print(res['clouds'])
    print(res['weather'])

# Data visualisation
#   


