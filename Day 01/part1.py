# Jefferson Henry 12/2/22
# https://adventofcode.com/2022/day/1

def main():
    largeSum = 0
    workingSum = 0
    with open('input.txt') as input:
        for line in input:
            if line == '\n':
                if workingSum > largeSum:
                    largeSum = workingSum
                workingSum = 0
            else:
                workingSum += int(line)
    print(largeSum)


if __name__ == '__main__':
    main()
