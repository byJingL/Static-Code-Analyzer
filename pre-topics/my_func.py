import math
import random

def greet(user_name, old=10, name=[]):
    today = 'Sunday'
    print("Hello, world!")
    print("Hello, ", user_name, "!", sep="")

def bye(username):
    print("Goodbye, world!")
    print("Goodbye, ", username, "!", sep="")

user = "Mary"
greet(user)
bye(user)