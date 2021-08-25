import os
import sys


def main():
    with open(r"C:\WINDOWS\system32\drivers\etc\services", 'r') as file:
        for line in file:
            if line.startswith('#') or line.isspace():
                continue
            splitted = line.split()
            port = int(splitted[1].split('/')[0])
            if 0 < port <= 200:
                print(line, end='')


if __name__ == "__main__":
    main()
