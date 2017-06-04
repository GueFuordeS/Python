#usr/bin/python3
from sys import argv

def pow(a, b):
    if b > 1:
        return a * pow(a, b-1)
    return a


if __name__ == '__main__':
    print(pow(int(argv[1]), int(argv[2])))
