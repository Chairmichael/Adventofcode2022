# Jefferson Henry 12/2/22
# https://adventofcode.com/2022/day/1#part2

def main():
    largeSums = [0, 0, 0]
    workingSum = 0
    with open('input.txt') as input:
        for line in input:
            if line == '\n':
                largeSums.append(workingSum)
                workingSum = 0
                largeSums.remove(min(largeSums))
            else:
                workingSum += int(line)
    print(sum(largeSums))


if __name__ == '__main__':
    main()
