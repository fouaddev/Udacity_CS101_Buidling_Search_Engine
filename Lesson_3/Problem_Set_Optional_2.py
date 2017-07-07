# ANTISYMMETRIC SQUARE

# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(matrix):
    converted_matrix = []
    for e in matrix:
        sub_converted_matrix = []
        for r in e:
            sub_converted_matrix.append(r * -1)
        converted_matrix.append(sub_converted_matrix)
    return converted_matrix == map(list, zip(*matrix))


# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False


###################################################################


# ANTISYMMETRIC SQUARE 1 LINE OF CODE SOLUTION:

def antisymmetric(matrix):
    return all(len(row) == len(matrix) for row in matrix) and all(matrix[e][r] == -matrix[r][e] for e in range(len(matrix)) for r in range(len(matrix)))


###################################################################


# RECOGNIZE IDENTITY MATRIX

