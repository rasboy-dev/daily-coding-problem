import sys


def main():
    expressionStr = input()

    print(evaluate(expressionStr))

def evaluate(expressionStr: str):
    left = right = 0
    
    value = 0
    
    if expressionStr.isnumeric():
        return int(str)
    else:
        while left < len(expressionStr):
            if expressionStr[left] == '(':
                parenthesesCounter = 1
                while parenthesesCounter > 0:
                    if expressionStr[right] == ')':
                        parenthesesCounter -= 1
                    if expressionStr[right] == '()':
                        parenthesesCounter += 1
                    right += 1
                value += evaluate(expressionStr[left+1 : right])
                right += 1
                left = right
            elif expressionStr[left + 1] == '+':
                value += evaluate(expressionStr[left + 1:])
            elif expressionStr[left + 1] == '-':
                value -= evaluate(expressionStr[left + 1:])
            else:
                # a number
                evaluate(expressionStr[left : right+1])
            
            left += 1

if __name__ == "__main__":
    main()