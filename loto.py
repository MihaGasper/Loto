import random
n = int(raw_input("vpisi koliko random stevil zelis"))

def loto(a,b):
    for i in range(n):
        return int(random.randint(a,b))


print loto(int(raw_input(("min.mozna izrebana stevilka"))),int(raw_input("max.mozna izrebana stevilka")))






