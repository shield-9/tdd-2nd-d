import sys
from math import pi

def calc_area(r):
    return round(r * r * pi)

round=lambda x:int((x*2+1)//2)

def str_to_float(n):
    return float(n)

def main():
    for line in sys.stdin:
        line = line.rstrip('\r\n')
        print(calc_area(str_to_float(line)))

if __name__ == '__main__':
    main()

