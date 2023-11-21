def det(matrix):
    print(f"given{matrix}")
    if len(matrix)<=2:
        topRow=matrix[0]
        bottomRow=matrix[0]
        return topRow[0]*bottomRow[0]-topRow[0]*topRow[0]

    else:
        cornerRow=matrix[0]

        matrixList=[]
        for i in range(len(matrix)-1):
            matrix0=matrix[:]
            matrix0=matrix0[1:]
            row=matrix0[0]
            row[i]=""
            
            for j in range(len(matrix0)):
                if row[j]=="":
                    for k in range(len(matrix0)):
                        row_to_remove=matrix0[k]
                        del row_to_remove[j]
                        matrix0[k]=row_to_remove
            print(matrix0)
            matrixList.append(matrix0)
        return cornerRow[0]*det(matrixList[0]) -cornerRow[1]*det(matrixList[1]) 




def main():
    
    row1=[1,2,3]
    row2=[-4,5,6]
    row3=[7,-8,9]
    matrixMain=[row1,row2,row3]
    
    print(det(matrixMain))
    
    
main()