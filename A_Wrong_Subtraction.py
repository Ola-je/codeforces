n, k= map(int, input().split())

for _ in range(k):
    if not n%10:
        n//=10
    else:
        n-=1
print(n)
