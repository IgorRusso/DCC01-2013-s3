def binomioRecursive(n,k):
    if n==k:
        return 1
    if k==0:
        return 1
    t1 = binomio(n-1,k-1)
    t2 = binomio(n-1,k)
    return t1+t2

def binomioDP(n,k):    
    matrix = [[0 for i in xrange(n+1)] for i in xrange(n+1)]
    for i in range(0,n+1):
        for j in range(0,k+1):
            if i==j or j==0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
    return matrix[n][k]