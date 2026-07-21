matrix=[[1,2,3,4],
        [2,3,4,5],
        [1,2,3,4],
        [1,2,3,4]]
rows=len(matrix)
column=len(matrix[0])
for i in range(0,rows):
    for j in range(0,column):
        if i+j== rows-1:
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ")
    print()



