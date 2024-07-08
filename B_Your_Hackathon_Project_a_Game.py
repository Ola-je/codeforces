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

n,m=mapinput()
arr=linput()
s_l=[0]
l_s=[0]*(n)

for i in range(n-1):
    if arr[i]>arr[i+1]:
        s_l.append(arr[i]-arr[i+1])
    else:
        s_l.append(0)

    if arr[n-i-1]>arr[n-i-2]:
        l_s[n-i-1]=(arr[n-i-1]-arr[n-i-2])
    else:
        l_s[n-i-1]=(0)

s_l.append(0)
l_s.append(0)

prefix_sum_s_l=[0]
prefix_sum_l_s=[0]

for i in range(1,n+1):
    prefix_sum_s_l.append(s_l[i]+prefix_sum_s_l[i-1])
    prefix_sum_l_s.append(l_s[i]+prefix_sum_l_s[i-1])

for _ in range(m):
    s,t=mapinput()
    if s<=t:
        print((prefix_sum_s_l[t]-s_l[t])-(prefix_sum_s_l[s]-s_l[s]))
    if s>t:
        print((prefix_sum_l_s[s]-l_s[s])-(prefix_sum_l_s[t]-l_s[t]))