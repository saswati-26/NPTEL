def magic_square(n):
    magic_square_matrix = [[0] * n for _ in range (n)]

    i = n // 2
    j = n - 1

    num = n * n
    element = 1

    while ( element <= num ):
        if ( i == -1 and j == n ):
            i, j = 0, n-2
        else:
            if ( i < 0 ):
                i = n - 1
            if ( j == n ):
                j = 0
        if ( magic_square_matrix[i][j] != 0 ):
            i += 1
            j -= 2
            continue

        else:
            magic_square_matrix[i][j] = element
            element += 1

        i -= 1
        j += 1

    for row in magic_square_matrix:
        for ele in row:
            print(ele , end =' ')
        print()

    print("Sum of row/column/diagonal: ", n * (n ** 2 + 1) // 2)

n = int(input("Enter n: "))            
magic_square(n)