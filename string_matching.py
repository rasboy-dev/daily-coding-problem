def build_table(pattern):
    matches = [0 for _ in range(len(pattern))]

    length = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[length]:
            length += 1
            matches[i] = length

        else:
            while length != 0:
                length = matches[length - 1]
            matches[i] = 0

    return matches

def main():
    str = 'AAAA'
    print(build_table(str), build_table(str) == [0, 1, 2, 3])
    str = 'ABCDE'
    print(build_table(str), build_table(str) == [0, 0, 0, 0, 0])
    str = 'AABAACAABAA'
    print(build_table(str), build_table(str) == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5])
    str = 'AAACAAAAAC'
    print(build_table(str), build_table(str) == [0, 1, 2, 0, 1, 2, 3, 3, 3, 4])
    str = 'AAABAAA'
    print(build_table(str), build_table(str) == [0, 1, 2, 0, 1, 2, 3])

if __name__ == '__main__':
    main()