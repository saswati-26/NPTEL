def multiply_matrix(matrix, scalar):
    return [[scalar * element for element in row] for row in matrix]

def parse_input():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    scalar = int(input())
    return matrix, scalar

def print_matrix(matrix):
    for i, row in enumerate(matrix):
        print(*row, end='')
        if i != len(matrix) - 1:
            print()  # Print a newline for all rows except the last one

if __name__ == "__main__":
    matrix, scalar = parse_input()
    result = multiply_matrix(matrix, scalar)
    print_matrix(result)
