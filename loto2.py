import random

def loto(a,b):
    return random.sample(range(a,b), int(raw_input("vpisi koliko random stevil zelis")))

print loto(int(raw_input("min.mozna izrebana stevilka")),int(raw_input("max.mozna izrebana stevilka")))