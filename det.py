def det(matrix):
    print(f"given{matrix}")
    if len(matrix)<=2:
        if len(matrix)==2:
            topRow=matrix[0]
            bottomRow=matrix[0]
            return 5
        else:
            return 0

    else:
        cornerRow=matrix[0]

        matrixList=[]
        matrix0=[]
        for i in range(len(matrix)):
            matrix0.append(matrix[i][:])
        
        matrix0=matrix0[1:]
        
        for i in range(len(matrix)):
            row=matrix0[0][:]
            row[i]="delete"
            print(f"matrix 0{matrix0}")
            print(row)
            print(matrix)
            matrixA=matrix0[:]
            for j in range(len(matrix0[0])):
                if j==i:
                    for k in range(len(matrix0)):
                        del matrixA[k][j]
                    break         
            print(f"YAY{matrixA}")
            matrixList.append(matrixA[:])
            matrix0=[]
            for i in range(len(matrix)):
                matrix0.append(matrix[i][:])
            matrix0=matrix0[1:]
        return 5

def main():
    row1=[1,2,3]
    row2=[-4,5,6]
    row3=[7,-8,9]
    matrixMain=[row1,row2,row3]
    
    print(det(matrixMain))
    
    
main()