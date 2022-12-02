# Jefferson Henry 12/2/22
# https://adventofcode.com/2022/day/2
# A for Rock, B for Paper, and C for Scissors (oponent)
# X for Rock, Y for Paper, and Z for Scissors (me)
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

def main():
    score = 0
    with open('input.txt') as input:
        for line in input:
            # ya i know this is bad =)
            oponent = ord(line.split()[0])
            me = ord(line.split()[1])
            diff = me - oponent - 23
            score += me - 87
            if diff == 0:
                score += 3
            elif diff == 1 or diff == -2:
                score += 6
    print(score)


if __name__ == '__main__':
    main()
