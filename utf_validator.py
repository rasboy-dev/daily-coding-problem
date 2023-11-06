import sys

def validate2(arr):    
    bytesCounter = 0
    for i in arr:
        leadingOnes = 0
        while i & 128:
            leadingOnes += 1
            i = i << 1

        if leadingOnes == 0:
            if bytesCounter:
                return False
        elif leadingOnes == 1:
            if not bytesCounter:
                return False
            bytesCounter -= 1
        else:
            if bytesCounter:
                return False
            bytesCounter = leadingOnes - 1
        
    return False if bytesCounter else True 

def main():
    arr = [int(i) for i in input().split()]
    print(validate2(arr))

if __name__ == "__main__":
    main()