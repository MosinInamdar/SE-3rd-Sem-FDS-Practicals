'''
Write a python program to compute the following computation on the matrix:
    1. Addition of Two Matrices         2. Subsraction of two Matrices
    3. Multiplication of two matrices   4. Transpose of a matrix
'''





def Add(mat1,mat2,row,column):
    mat3=[[0,0,0],[0,0,0],[0,0,0]]
    print("Addition of the two matrices is : ")
    for i in range (row):
        for j in range (column):
            mat3[i][j]=mat1[i][j]+mat2[i][j]
            print(mat3[i][j],end=' ')
        print()




def Sub(mat1,mat2,row,column):
    mat3 = [[0,0,0],[0,0,0],[0,0,0]]
    print("Subsraction of the two matrices is : ")
    for i in range(row):
        for j in range(column):
            mat3[i][j] = mat1[i][j] - mat2[i][j]
            print(mat3[i][j],end=' ')


def transpose():
    mat = []
    row = int(input("Enter the Size of Row In Matrix : "))
    column = int(input("Enter the Size of Column In Matrix : "))
    print("Enter Elements in matrix : ")
    for i in range(row):
        a=[]
        for j in range(column):
            x = int(input())
            a.append(x)
        mat.append(a)

    print("Matrix : ")
    for i in range(row):
        for j in range(column):
            print(mat[i][j], end=' ')
        print()


    print("Transpose of Matrix 1 : ")
    for i in range(row):
        for j in range(column):
            print(mat[j][i],end=' ')
        print()

def mul(mat1,mat2,row,column):
    mat3=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(mat1)):
        for j in range (len(mat2[0])):
            for k in range (len(mat2)):
                mat3[i][j]+=mat1[i][k]*mat2[k][j]
    print("Multiplied Matix : ")
    for i in range (row):
        for j in range (column):
            print(mat3[i][j],end=' ')
        print()


# main function

print("\n\n*********Manu Matrix *************")
print("\n 1. Addition of Two Matrices \n 2.Subsraction of Two Matrices \n 3. Transpose of a Matrix \n 4. Matix Multipication")
print("\nPress : ")
choice=int(input())

if choice == 1:
    mat1 = []
    row1 = int(input("Enter the Size of Row In Matrix 1 : "))
    column1 = int(input("Enter the Size of Column In Matrix 1 : "))
    print("Enter Elements in matrix : ")
    for i in range(row1):
        a = []
        for j in range(column1):
            a.append(int(input()))
        mat1.append(a)

    print("Matrix 1 : ")
    for i in range(row1):
        for j in range(column1):
            print(mat1[i][j], end=' ')
        print()

    mat2 = []
    row2 = int(input("Enter the Size of Row In Matrix 2 : "))
    column2 = int(input("Enter the Size of Column In Matrix 2 : "))
    print("Enter Elements in matrix : ")
    for i in range(row1):
        a = []
        for j in range(column1):
            a.append(int(input()))
        mat2.append(a)

    print("Matrix 2 : ")
    for i in range(row1):
        for j in range(column1):
            print(mat2[i][j], end=' ')
        print()

    if row1==row2 and column1==column2 :
        Add(mat1,mat2,row1,row2)
    else :
        print("Matices can't be subsracted as rows and columns dont match!!")

elif choice==2:
    mat1 = []
    row1 = int(input("Enter the Size of Row In Matrix 1 : "))
    column1 = int(input("Enter the Size of Column In Matrix 1 : "))
    print("Enter Elements in matrix : ")
    for i in range(row1):
        a = []
        for j in range(column1):
            a.append(int(input()))
        mat1.append(a)

    print("Matrix 1 : ")
    for i in range(row1):
        for j in range(column1):
            print(mat1[i][j], end=' ')
        print()

    mat2 = []
    row2 = int(input("Enter the Size of Row In Matrix 2 : "))
    column2 = int(input("Enter the Size of Column In Matrix 2 : "))
    print("Enter Elements in matrix : ")
    for i in range(row1):
        a = []
        for j in range(column1):
            a.append(int(input()))
        mat2.append(a)

    print("Matrix 2 : ")
    for i in range(row1):
        for j in range(column1):
            print(mat2[i][j], end=' ')
        print()
    if row1==row2 and column1==column2 :
        Sub(mat1, mat2, row1, column1)
    else :
        print("Matices can't be subsracted as rows and columns dont match!!")


elif choice==3:
    transpose()
elif choice==4:
    mat1 = []
    row1 = int(input("Enter the Size of Row In Matrix 1 : "))
    column1 = int(input("Enter the Size of Column In Matrix 1 : "))
    print("Enter Elements in matrix : ")
    for i in range(row1):
        a = []
        for j in range(column1):
            a.append(int(input()))
        mat1.append(a)

    print("Matrix 1 : ")
    for i in range(row1):
        for j in range(column1):
            print(mat1[i][j], end=' ')
        print()

    mat2 = []
    row2 = int(input("Enter the Size of Row In Matrix 2 : "))
    column2 = int(input("Enter the Size of Column In Matrix 2 : "))
    print("Enter Elements in matrix : ")
    for i in range(row1):
        a = []
        for j in range(column1):
            a.append(int(input()))
        mat2.append(a)

    print("Matrix 2 : ")
    for i in range(row1):
        for j in range(column1):
            print(mat2[i][j], end=' ')
        print()

    if row1==column2:
        mul(mat1,mat2,row1,column1)
    else:
        print("Matrix Multipication not possible")
else:
    print("wrong input")

