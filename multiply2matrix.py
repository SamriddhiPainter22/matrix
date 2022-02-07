#define two matrix A and B in program

A= [[5,4,3],
[2,3,1],
[4,7,9]]

B=[[3,4,2],
[4,3,6],
[2,7,5]]

#Define an empty matrix to store multiplication result

multiResult = [[0,0,0],
[0,0,0],
[0,0,0]]


#using nested for loop method on A & B matrix

for m in range (len(A)):
    for n in range(len(B[0])):
        for o in range(len(B)):
             multiResult[m][n]  += A[m][o] * B[o][n]

#Storing multiplication result in empty matrix 
#Printing multiplication result in output

print("The multiplication result of matrix A and B is : ")
for res  in multiResult:
    print(res)
