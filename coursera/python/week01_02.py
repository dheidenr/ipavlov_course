import sys

num = int(sys.argv[1])
for step in range(1, num + 1):
    print(" " * (num - step) + "#" * (num - (num - step)))
