from collections import defaultdict, deque
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


n=intinput()
graph=defaultdict(list)
root=0
for i in range(n):
    p,c=mapinput()

    if p==-1:
        root=i+1
        continue

    graph[p].append((i+1,c))

temp=deque([(root,0)])
queue=deque()

while temp:
    node=temp.popleft()

    for p,c in graph[node[0]]:
        if c==1:
            queue.append(p)

        temp.append((p,c))


ans=[]
temp=[]
leaves=[]
i=1

while queue:
    count=0
    node=queue.popleft()

    for p,c in graph[node]:
        if c==1:
            count+=1

    if len(graph[node])==count:
        if count==0:
            leaves.append((count,i,node))
        else:
            temp.append((count,i,node))

    i+=1

temp.sort()
leaves.sort()

for c,i,n in temp:
    if c>1:
        for c2,i2,n2 in leaves:
            ans.append(n2)
        leaves=[]

    ans.append(n)
if leaves:
    for c,i,n in leaves:
        ans.append(n)
if ans:
    print(*ans)
else:
    print(-1)