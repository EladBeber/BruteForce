# Bruteforce tool by EdbR
import itertools

# 1.Numbers - 0123456789
def Numbers(Numbers):
    for i in range(48, 58):
        Numbers.append(chr(i))

# 2.UpperCase - ABCDEFGHIJKLMNOPQRSTUVWXYZ
def UpperCase(UpperCase):
    for i in range(65, 91):
        UpperCase.append(chr(i))

# 3.lowerCase - abcdefghijklmnopqrstuvwxyz
def lowerCase(lowerCase):
    for i in range(97, 123):
        lowerCase.append(chr(i))

# 4.Bruteforce - All the options - (len(list) ^ LenOfFlag)
def Bruteforce(list,LenOfFlag):
    iterator=itertools.product(list,repeat=LenOfFlag)
    for i in iterator:
        flag="".join(i)
        print(flag)
