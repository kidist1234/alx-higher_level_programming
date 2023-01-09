#!/usr/bin/python3
if __name__ == "__main__":
    import sys
number = len(sys.argv)
count = number - 1
if number == 1:
    print("{} arguments.".format(count))
elif number == 2:
    print("{} argument:".format(count))
else:
    print("{} arguments:".format(count))
for i in range(1, number):
    print("{}: {}".format(i, sys.argv[i]))
