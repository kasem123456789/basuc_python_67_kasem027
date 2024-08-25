"""
#
# Part: Python JSON
# API=Application Programming Inter
#
"""

import json
#make a json (Dictionary string)
x='{"name":"john","age":20,"city":"Phuket"}'
print(x)
# parse
 
y=json.loads(x)

#python dictonary
print(y)
print(type(y))
print(y["city"])

#python dictonary
a={
    "name":"Noa",
    "age":20,
    "city":"Phuket"
}
# convert to JSON (String)
b=json.dumps(a)
#JSON String
print(d)
