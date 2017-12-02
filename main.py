from math import inf
import main1


def Greedy(a, b):
    M = len(a)
    N = len(b)
    mat = 4
    mis = -2
    ind = -4
    X = 2**(abs(M-N)+1)+max(M,N)/8 # max difference after which we do not involve current in next score

    def SPrime(i, j, d):
        """
        computes score
        :param i: ind dna 1
        :param j: ind dna 2
        :param d: num of dif
        :return: score
        """
        return ((i + j + 2) * mat / 2) - d * (mat - mis)  # can be done like lambda

    i = 0
    R = [{i:-inf for i in range(-max(M, N), max(M, N) + 1)} for _ in range(max(M, N) + 1)]
    T = [0 for _ in range(max(M, N) + 1)]  # all best results

    while (i < min(M, N)) and (a[i] == b[i]):  # cuts same beginning
        i += 1
    if i == min(M, N):  # if on edna is a part of another return max score
        return mat * min(M, N) * 1.0
    R[0][0] = i

    TPrime = SPrime(i-1, i-1, 0)

    T[0] = TPrime
    d = 0
    L = 0
    U = 0

    while L <= U + 2:
        d += 1
        if d > max(M, N):  # there is no sense to count more difs then nucls in dna
            return TPrime
        dprime = int(max((d - int((X + mat / 2) / (mat - mis)) - 1), 0))

        for k in range(L - 1, U + 2):

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

            i = max(firstI, secondI, thirdI)
            j = i - k
            if (i > -inf) and (SPrime(i, j, d) >= (T[dprime] - X)):
                # if cell is not empty and the score is good enough ^ strip next identical part
                # print("Hello there")
                while (i < M - 1) and (j < N - 1) and (a[i] == b[j]):
                    i += 1
                    j += 1
                R[d][k] = i
                # print(R[d][k],d,k,i)
                TPrime = max(TPrime, SPrime(i, j, d))
            else:
                # print(R[d][k], d, k, i)
                R[d][k] = -inf

        T[d] = TPrime

        for k in range(-max(M, N), max(M, N)+1):
            if R[d][k] > - inf:
                L = k
                break

        for k in reversed(range(-max(M, N), max(M, N)+1)):
            if R[d][k] > - inf:
                U = k
                break

        for k in reversed(range(-max(M, N), max(M, N)+1)):
            if R[d][k] == N + k:
                L = max(L, k + 2)
                break

        for k in range(-max(M, N), max(M, N)+1):
            if R[d][k] == M:
                U = min(U, k - 2)
                break
    return TPrime


# a = "AACCTXXGAACCTTGG"
# b = "AACCTTGGAACCTTGG"
# print(Greedy(a, b))
lst = []
for _ in range(100):
    a = main1.DNAgenerator(80)
    b = main1.DNAchanger(a, 0.1)
    lst.append(Greedy(a, b))
print(sorted(lst))
