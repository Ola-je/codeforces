import sys

def intinput():
    return int(sys.stdin.readline().strip())

def string():
    return sys.stdin.readline().strip()

def linput():
    return list(map(int, sys.stdin.readline().strip().split()))

def digitlist():
    return [int(i) for i in list(sys.stdin.readline().strip())]

def charlist():
    return list(sys.stdin.readline().strip())

def mapinput():
    return map(int, sys.stdin.readline().strip().split())


for _ in range(intinput()):
    n=intinput()
    s=string()
    c=0

    for i in range(n-1,-1,-1):
        if s[i] != ')':
            break
        else:
            c+=1

    if c>len(s[:n-c]):
        print('Yes')
    else:
        print('No')