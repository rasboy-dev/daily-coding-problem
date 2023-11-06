import sys

def main():
    n = int(input())
    brickRows = []
    for row in sys.stdin.readlines():
        brickRow = [int(brick) for brick in row.split()]
        brickRows.append(brickRow)

    length = sum(brickRows[0])
    cuts = [0] * (length - 1)
    for i in range(0, n):
        cur = 0
        for brickLength in brickRows[i]:
            for _ in range(0, brickLength - 1):
                cuts[cur] += 1
                cur += 1
            cur += 1

    print(cuts)
    print(min(enumerate(cuts), key=lambda x: x[1]))

if __name__ == "__main__":
    main()