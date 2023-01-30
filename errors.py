#!/usr/bin/env python3
import os
import sys

#EAFP - Easy to Ask Forgiveness than Permission
# (È mais fácil pedir perdão do que permissão)

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print("\033[31m[Error]\033[m Missing name in the list")
    sys.exit(1)
        