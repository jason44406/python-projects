# Returns every possible permiation of an array [i,k,j] with elements who's sum is not equal to n and values up to [x,y,z].

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print( [ [ i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range (z + 1)
    if ((i + j + k) != n )])
