n, m = map(int, input().split())
elements = list(map(int, input().split()))
A = set([int(x) for x in input().split() if int(x) in elements])
B = set([int(x) for x in input().split() if int(x) in elements])

print(len(A) - len(B))
