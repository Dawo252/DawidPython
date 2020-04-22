A = [1/x for x in range(11) if x!=0]
print(A)
B = [2**x for x in range(11)]
print(B)
C = [x for x in B if x%4==0]
print(C)