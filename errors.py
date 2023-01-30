#!/usr/bin/env python3

import os
import sys

if os.path.exists("names.txt"):
    print("O arquivo existe")
    input("...")
    names = open("names.txt").readlines()
else:
    print("\033[31m[Error]\033[m File names.txt not found")
    sys.exit(1)


if len(names) >= 3:
    print(names[2])
else:
    print("\033[31m[Error]\033[m Missing name in the list")
    sys.exit(1)
        