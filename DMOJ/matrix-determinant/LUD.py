import sys
input = sys.stdin.readline
M = 1000000007
N = int(input())
ARR = [[int(x) for x in input().split()] for j in range(N)]

def LU(A):
    
    # (1) Extract the b vector
    b = [0 for i in range(N)]
    for i in range(0,N):
        b[i]=A[i][N]

    # (2) Fill L matrix and its diagonal with 1
    L = [[0 for i in range(N)] for i in range(N)]
    for i in range(0,N):
        L[i][i] = 1

    # (3) Fill U matrix
    U = [[0 for i in range(0,N)] for i in range(N)]
    for i in range(0,N):
        for j in range(0,N):
            U[i][j] = A[i][j]

    n = len(U)

    # (4) Find both U and L matrices
    for i in range(0,N): # for i in [0,1,2,..,n]
        # (4.1) Find the maximun value in a column in order to change lines
        maxElem = abs(U[i][i])
        maxRow = i
        for k in range(i+1, n): # Interacting over the next line
            if(abs(U[k][i]) > maxElem):
                maxElem = abs(U[k][i]) # Next line on the diagonal
                maxRow = k

        # (4.2) Swap the rows pivoting the maxRow, i is the current row
        for k in range(i, n): # Interacting column by column
            tmp=U[maxRow][k]
            U[maxRow][k]=U[i][k]
            U[i][k]=tmp

        # (4.3) Subtract lines
        for k in range(i+1,n):
            c = -U[k][i]/float(U[i][i])
            L[k][i] = c # (4.4) Store the multiplier
            for j in range(i, n):
                U[k][j] += c*U[i][j] # Multiply with the pivot line and subtract

        # (4.5) Make the rows bellow this one zero in the current column
        for k in range(i+1, n):
            U[k][i]=0

    n = len(L)

    # (5) Perform substitutioan Ly=b
    y = [0 for i in range(n)]
    for i in range(0,n,1):
        y[i] = b[i]/float(L[i][i])
        for k in range(0,i,1):
            y[i] -= y[k]*L[i][k]

    n = len(U)

    # (6) Perform substitution Ux=y
    x = [0 in range(n)]
    for i in range(n-1,-1,-1):
        x[i] = y[i]/float(U[i][i])
        for k in range (i-1,-1,-1):
            U[i] -= x[i]*U[i][k]

    return x

print(LU(ARR))