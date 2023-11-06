import sys

def main():
    initialConditions = input()

    hasRightPressure = False
    dominosInProcessing = 0
    result = ''
    for i in range(0, len(initialConditions)):
        if initialConditions[i] == 'L':
            dominosInProcessing += 1
            result += process(dominosInProcessing, hasRightPressure, True)
            dominosInProcessing = 0
            hasRightPressure = False
        elif initialConditions[i] == 'R':
            result += process(dominosInProcessing, hasRightPressure, False)
            dominosInProcessing = 1
            hasRightPressure = True
        else:
            dominosInProcessing += 1
    
    result += process(dominosInProcessing, hasRightPressure, False)
    print(result)
    

def process(numberOfDominos, hasRightPressure, hasLeftPressure):
    if hasRightPressure and hasLeftPressure:
        half = numberOfDominos // 2
        return 'R' * half + ('.' if numberOfDominos % 2 != 0 else '') + 'L' * half
    elif hasRightPressure:
        return 'R' * numberOfDominos
    elif hasLeftPressure:
        return 'L' * numberOfDominos
    else:
        return '.' * numberOfDominos
    

if __name__ == '__main__':
    main() 