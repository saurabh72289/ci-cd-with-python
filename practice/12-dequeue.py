from collections import deque

dq = deque()
dq.append(12) # it will append on right side
dq.append(13)
dq.append(14)

print(dq)


dq.appendleft(120) # it will append on left sideprint

print(dq)

dq.popleft()
print(dq)

dq.pop()
print(dq)