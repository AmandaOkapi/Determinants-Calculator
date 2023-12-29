import copy
def det(matrix):
    #print(f"given{matrix}")
    

    
    if len(matrix)<=2:
        return matrix[0][0] *matrix[1][1] - (matrix[1][0] * matrix[0][1])

    else:
        #to store each submatrix
        subMatrixList=[]
        
        #make the submatricies

        for i in range(len(matrix)):
            #remove the first row
            subMatrix=copy.deepcopy(matrix[1:])
            #print(subMatrix)
            #make each subMatrix and append to a list
            for j in range(len(matrix)):
                #remove the collumn to form the submatrix
                if j==i:
                    for k in range(len(subMatrix)):
                        #print(f" deleting{subMatrix[k][j]}")
                        del subMatrix[k][j]
                    break         
            #print(f"submatrix{ i }: { subMatrix}")
            subMatrixList.append(copy.deepcopy(subMatrix))

        #print(subMatrixList)

        #calculate the determinant 
        detTotal=0
        row0=matrix[0][:]
        
        for i in range(len(row0)):
            if row0[i] != 0:
                detTotal+=(row0[i] * det(subMatrixList[i])) * ((-1)**i)

        return detTotal

def main():
    
    #user inputs
    while True:
        n=int(input("Enter a matrix dimension: "))
        if n>=2:
            break
        else:
            print("Dimension must be at least 2")
    
    matrixMain=[]
    for i in range(n):
        print(f"Enter values for row{i+1}: ")
        row=[]
        for j in range(n):
            while True:
                x=input(f"val{i+1},{j+1}: ")
                try:
                    x=int(x)
                    row.append(x)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid integer.")
        matrixMain.append(row[:])
        for k in range(len(matrixMain)):
            print (matrixMain[k])


    
    print(det(matrixMain))
    
    
main()