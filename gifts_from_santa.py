N = int(input()) # 0 <= N < M
M = int(input()) # N < M <= 10000
S = int(input()) # N <= S <= M

if N in range(0, 10000) and S in range(0, 10001) and M in range(1, 10001):
    for numbers in range(M, N + 1, -1):
        if numbers % 2 == 0 and numbers % 3 == 0:
            if numbers == S:
                break
            print(numbers, end=" ")
