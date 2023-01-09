#!/usr/bin/python3
if __name__ == "__main__":
    import sys
number = len(sys.argv)
total_sum = 0
for i in range(1, number):
    total_sum += int(sys.argv[i])
print("{}".format(total_sum))
