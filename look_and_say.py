import sys

def main():
    pass

    n = 1
    nth = 5

    term = str(n)
    for i in range(1, nth):
        nextTerm = []
        curChar = ''
        curCharCounter = 0
        for char in term:
            if char == curChar:
                curCharCounter += 1
            else:
                if curChar:
                    nextTerm.append(str(curCharCounter) + curChar)
                curChar = char
                curCharCounter = 1
        nextTerm.append(str(curCharCounter) + curChar)
        term = ''.join(nextTerm)
        print(term)

    print()
    print(term)
if __name__ == "__main__":
    main()