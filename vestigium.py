cases = int(input())


#iterate over cases
for c in range(cases):
    trace=0
    size = int(input())
    matrix = []
    #Fill Matrix
    for i in range(size):
        matrix.append(input().split())

    #Calculate trace
    for i in range(size):
        trace += int(matrix[i][i])

    #Get row repetead elements
    row_repetead = 0
    for i in range(size):
        row_dict = {}
        for j in range(size):
            if( matrix[i][j] in row_dict):
                row_repetead += 1
                break
            else:
                row_dict[ matrix[i][j] ] = 0

    #Get column repetead elements
    column_repetead = 0
    for i in range(size):
        column_dict = {}
        for j in range(size):
            if( matrix[j][i] in column_dict):
                column_repetead += 1
                break
            else:
                column_dict[ matrix[j][i] ] = 0
    

    print('Case #{}: {} {} {}'.format(c+1, trace, row_repetead, column_repetead))
    