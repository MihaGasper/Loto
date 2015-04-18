import random
list =[]
n = int(raw_input("vpisi koliko random stevil zelis"))

def loto(a,b):
    for i in range(n):
        list.append(int(random.randint(a,b)))
    return (list)


print loto(int(raw_input(("min.mozna izrebana stevilka"))),int(raw_input("max.mozna izrebana stevilka")))






