import sys

from collections import deque

n = int(input()) + 1
connectionsStr = sys.stdin.readlines()
connections = {}
for i in range(0, n):
    connections[i] = []
for connection in connectionsStr:
    connection = connection.rstrip().split()
    connection = [int(i) for i in connection]
    connections[connection[0]].append(connection[1:3])

visited = set()
toBeVisited = set()
times = []
for i in range(0, n):
    toBeVisited.add(i)
    times.append(sys.maxsize)
times[0] = 0
while len(toBeVisited) > 0:
    node = min(toBeVisited, key=lambda x: times[x])
    for i, time in connections[node]:
        times[i] = min(times[i], times[node] + time)
    visited.add(node)
    toBeVisited.remove(node)

print(max(times))


