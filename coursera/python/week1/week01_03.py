import sys
import random

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

print(str(int((-b + (b ** 2 - 4 * a * c) ** 0.5)/(2 * a))))
print(str(int((-b - (b ** 2 - 4 * a * c) ** 0.5)/(2 * a))))

for x in range(4):
    print(x)
