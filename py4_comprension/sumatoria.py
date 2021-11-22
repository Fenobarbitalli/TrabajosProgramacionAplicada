A=[1,2,3]
B=[2,4,6]
C=[3,6,9]

n=len(A)

print(sum((A[i]*B[i]+C[i]) for i in range(n))* n**2)