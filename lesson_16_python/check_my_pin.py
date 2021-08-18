#!/usr/bin/python
import getpass

PIN = '1234'
password = ''

for i in range(3):
    password = getpass.getpass(prompt="Input PIN:")
    # password = input("Input PIN:")
    if password == PIN:
        break
if password == PIN:
    print("Success!")
else:
    print("Failure!")
