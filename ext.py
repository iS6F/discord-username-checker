from config import *
from requests import post
from string import ascii_letters, digits
from time import sleep
from json import dumps
from random import choice
with open('tokens.txt', 'r') as f: k = f.read().splitlines()
a = lambda num: ''.join(choice(ascii_letters.lower() + digits + "._") for x in range(0,num))
l = lambda num: ''.join(choice(ascii_letters.lower()) for x in range(0,num))
d = lambda num: ''.join(choice(digits) for x in range(0,num))
r = 0
q = False