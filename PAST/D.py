X, Y = map(int, input().split())
X_divis = [i for i in range(1, X+1) if X % i ==0]
Y_divis = [i for i in range(1, Y+1) if Y % i ==0]

if len(X_divis) == len(Y_divis):
    ans = "Z"
elif len(X_divis) > len(Y_divis):
    ans = "X"
else:
    ans = "Y"
print(ans)