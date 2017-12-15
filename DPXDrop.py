from math import inf


def Dynamic(a, b):
    def S(i, j):
        if (i < 0 or j < 0):
            return -inf
        return s[int(i * 2)][int(j * 2)]

    def setS(i, j, v):
        if not (i < 0 or j < 0):
            s[int(i * 2)][int(j * 2)] = v

    M = len(a) - 1
    N = len(b) - 1
    mat = 4
    mis = -2
    ind = -4
    X = max(int(len(a) / 10), 6)
    s = [[-inf for _ in range(N * 6)] for _ in range(M * 6)]
    T = 0
    TPrime = 0
    k = 0
    L = 0
    U = 0
    s[0][0] = 0

    while L <= U + 1:
        k += 1
        # if k > min(M*2,N*2)-1:
        #     break
        i = L // 1 + L % 1 * 2
        while (i <= int(U + 1)):
            # print(i)
            j = k - i
            if i % 1 == 0:
                firstI = -inf
                secondI = -inf
                thirdI = -inf
                forthI = -inf
                # print(d,k,L,U,TPrime)
                if L <= i - 0.5 and i - 0.5 <= U:
                    if a[int(i)] == b[int(j)]:
                        firstI = S(i - 0.5, j - 0.5) + mat / 2
                    else:
                        secondI = S(i - 0.5, j - 0.5) + mis / 2
                if i <= U:
                    thirdI = S(i, j - 1) + ind
                if L <= i - 1:
                    forthI = S(i - 1, j) + ind

                setS(i, j, max(firstI, secondI, thirdI, forthI))
            else:
                setS(i, j, S(i - 0.5, j - 0.5) + (mat / 2 if a[int(i + 0.5)] == b[int(j + 0.5)] else mis / 2))
            TPrime = max(TPrime, S(i, j))
            if S(i, j) < T - X:
                setS(i, j, -inf)
            i += 0.5
        # print("LU",L,U)
        o = 0
        while o <= k:
            if S(o, k - o) > - inf:
                L = o
                break
            o += 0.5
        o = k
        while o >= 0:
            if S(o, k - o) > - inf:
                U = o
                break
            o -= 0.5
        # print("LU",L,U)
        L = max(L, k + 1 - N)
        U = min(U, M - 1)
        # print("LU",L,U)
        T = TPrime
    # for i in s:
    #     print(i)

    return TPrime
