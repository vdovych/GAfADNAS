from math import inf
for k in range(max(M, N)):
    if R[d][k] > - inf:
        L = k
        break

for k in reversed(range(max(M, N))):
    if R[d][k] > - inf:
        U = k
        break

for k in reversed(range(max(M, N))):
    if R[d][k] == N + k:
        L = max(L, k + 2)
        break

for k in range(max(M, N)):
    if R[d][k] == M:
        U = min(U, k - 2)
        break
