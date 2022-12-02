# Jefferson Henry 12/2/22
# https://adventofcode.com/2022/day/2#part2
# A for Rock, B for Paper, and C for Scissors (oponent)
# X means you need to lose,
# Y means you need to draw,
# Z means you need to win
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

def main():
    score = 0
    with open('input.txt') as input:
        for line in input:
            # probably just as bad
            oponent = ord(line.split()[0])
            result = ord(line.split()[1])
            score += (result - 88) * 3
            l = [1, 2, 3]
            try:
                score += l[oponent-65 + result-89]
            except:
                score += 1
    print(score)


if __name__ == '__main__':
    main()
