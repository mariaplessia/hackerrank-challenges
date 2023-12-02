from itertools import product

K, M = map(int,input().split())

N = (list(map(int, input().split()))[1:] for _ in range(K))

max_list = []
for item in product(*N):
    S = 0
    for val in item:
        S += val**2
    S_maximized = S % M
    max_list.append(S_maximized)
    
print(max(max_list))
