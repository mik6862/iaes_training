# from Konstantin(Kostua)
import sys

def hello(user):
	print "Hello "+user+"!"

def getUser(user):
    try:
        return sys.argv[1]
    except:
        return user

def Main():
    x=getUser("World")
    hello(x)

Main()