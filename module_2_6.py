import random
n = random.randint(3, 20)
kod = ''
for k in range(1, n):
    for j in range(2, n):
        if j<= k:
            continue
        if n % (k + j) == 0:
            kod += str(k) + str(j)
print(n)
print('Код подобран:', kod)

