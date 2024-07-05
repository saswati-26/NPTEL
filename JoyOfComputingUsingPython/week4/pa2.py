def matrix_product(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def parse_input():
    n = int(input())
    
    # A = [list(map(int, input().split(','))) for _ in range(n)]
    A = []
    for _ in range (n):
        row = input().split(',')
        row = [int(num) for num in row]
        A.append(row)
    
    # B = [list(map(int, input().split(','))) for _ in range(n)]
    B = []
    for _ in range(n):
        row = input().split(',')
        row = [int(num) for num in row]
        B.append(row)
    return A, B


def print_matrix(matrix):
    for i, row in enumerate(matrix):
        print(','.join(map(str, row)), end='')
        if i != len(matrix) - 1:
            print()


if __name__ == "__main__":
    A, B = parse_input()
    result = matrix_product(A, B)
    print_matrix(result)