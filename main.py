from math import inf
import main1


def Greedy(a, b):
    M = len(a)
    N = len(b)
    mat = 4
    mis = -2
    ind = -4
    X = 2

    def SPrime(i, j, d):
        return ((i + j) * mat / 2) - d * (mat - mis)  # can be done like lambda

    i = 0
    R = [[-inf] * (max(M, N) + 1) for _ in range(max(M, N) + 1)]
    T = [0 for _ in range(max(M, N) + 1)]

    while (i < min(M, N)) and (a[i] == b[i]):
        i += 1
    if i == min(M, N):
        return mat * min(M, N) * 1.0
    R[0][0] = i

    TPrime = SPrime(i, i, 0)

    T[0] = TPrime
    d = 0
    L = 0
    U = 0

    while L <= U + 2:
        d += 1
        if d> min(M,N):
            return TPrime
        dprime = int(max((d - int((X + mat / 2) / (mat - mis)) - 1), 0))

        for k in range(max(0, L - 1), U + 1):
            firstI = -inf
            secondI = -inf
            thirdI = -inf
            # print(d,k,L,U,TPrime)
            if L < k:
                firstI = R[d - 1][k - 1] + 1

            if (L <= k) and (k <= U):
                secondI = R[d - 1][k] + 1

            if k < U:
                thirdI = R[d - 1][k + 1]

            i = max(firstI, max(secondI, thirdI))
            j = i - k
            if (i > -inf) and (SPrime(i, j, d) >= (T[dprime] - X)):

                while (i < M - 1) and (j < N - 1) and (a[i] == b[j]):
                    i += 1
                    j += 1
                R[d][k] = i
                TPrime = max(TPrime, SPrime(i, j, d))
            else:
                R[d][k] = -inf

        T[d] = TPrime

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
    return TPrime


lst = []
for _ in range(100):
    a = main1.DNAgenerator(40)
    b = main1.DNAchanger(a, 0.1)
    lst.append(Greedy(a, b))
print(sorted(lst))
