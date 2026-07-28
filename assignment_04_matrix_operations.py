# Function to read a matrix
def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


# Function to display a matrix
def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()


# Part A: Transpose a matrix
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose


# Part B: Add two matrices
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


# Part C: Multiply two matrices
def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = []

    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            total = 0
            for k in range(cols_A):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)

    return result


# ==========================
# PART A
# ==========================
print("PART A - Transpose Matrix")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols)

print("\nOriginal Matrix:")
display_matrix(matrix)

print("\nTransposed Matrix:")
display_matrix(transpose_matrix(matrix))


# ==========================
# PART B
# ==========================
print("\nPART B - Add Two Matrices")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter Matrix 1")
matrix1 = read_matrix(rows, cols)

print("Enter Matrix 2")
matrix2 = read_matrix(rows, cols)

print("\nSum of Matrices:")
display_matrix(add_matrices(matrix1, matrix2))


# ==========================
# PART C
# ==========================
print("\nPART C - Multiply Two Matrices")

rows_A = int(input("Enter rows for Matrix A: "))
cols_A = int(input("Enter columns for Matrix A: "))

print("Enter Matrix A")
A = read_matrix(rows_A, cols_A)

rows_B = int(input("Enter rows for Matrix B: "))
cols_B = int(input("Enter columns for Matrix B: "))

if cols_A != rows_B:
    print("Error: Number of columns in Matrix A must equal number of rows in Matrix B.")
else:
    print("Enter Matrix B")
    B = read_matrix(rows_B, cols_B)

    print("\nProduct of Matrices:")
    display_matrix(multiply_matrices(A, B))