import sys

def main():
    n = int(input())
    friendshipList = {}
    for i in range(0, n):
        friendshipList[i] = []
        for j in [int(f) for f in input().split()]:
            friendshipList[i].append(j)

    determined = set()
    friendGroups = []
    for i in range(0, n):
        if i not in determined:
            friendGroup = set()
            dfs(i, friendshipList, friendGroup)
            for f in friendGroup:
                determined.add(f)
            friendGroups.append(friendGroup)

    print(friendGroups)

def dfs(i, friendshipList, friendGroup):
    friendGroup.add(i)
    for f in friendshipList[i]:
        if f not in friendGroup:
            friendGroup.add(f)
            dfs(f, friendshipList, friendGroup)

if __name__ == "__main__":
    main()