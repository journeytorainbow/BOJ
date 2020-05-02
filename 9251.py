import sys 

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

array = [[0]*(len(A)+1) for _ in range(len(B)+1)]

for i in range(0, len(B)):
    for j in range(0, len(A)):
        if A[j] == B[i]:
            array[i+1][j+1] = array[i][j] + 1
        else:
            array[i+1][j+1] = max(array[i][j+1], array[i+1][j])

print(array[len(B)][len(A)])