from .rusty_bits import hello
import sys

def say_hello():
    name = sys.argv[1]
    hello(name)
