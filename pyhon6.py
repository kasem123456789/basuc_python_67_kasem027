"""
#
# Part: Python Function
#
"""
def myFunction():
    i = 1
    while i <= 5:
        print("Hello World",i)
        i+=1
myFunction()
myFunction()

def myName(name):

    print("My name is "+ name)
myName("เกษม")

def myFullName(fullname ="Unknown",fulllname ="Forger"):
    print("My name is "+ fullname+" "+fulllname)
myFullName("เกษม","เกษมสุข")
myFullName("ขยะ","ขยะ1")

def myFruit(fruits):
    for fruit in fruits:
        print(fruit)
fruits = ["Apple","Banana","Coconut"]
myFruit(fruits)

def redPotion(hp):
    return hp + 50
print("HP:",redPotion(100))
print("HP:",redPotion(30))