def hvlcs(A, B, values):
    n = len(A)
    m = len(B)

    # grid of zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill in grid
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                # chars match
                dp[i][j] = dp[i - 1][j - 1] + values.get(A[i - 1], 0)
            else:
                # No match — take the better option
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # backtracking
    i, j = n, m
    subseq = []
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            subseq.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    subseq.reverse()
    return dp[n][m], "".join(subseq)

# reads input
K = int(input())
values = {}
for _ in range(K):
    ch, val = input().split()
    values[ch] = int(val)

A = input().strip()
B = input().strip()

max_value, subsequence = hvlcs(A, B, values)
print(max_value)
print(subsequence)
