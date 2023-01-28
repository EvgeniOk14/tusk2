m = int(input())
n = int(input())
k = int(input())
print('m равно: ', m)
print('n равно: ', n)
print('k равно: ', k)
if (k < m*n and k % m == 0 or k % n == 0):
    print(' yes')
else:
    print(' no')

