user_input = input().split()
n = int(user_input[0])
m = int(user_input[1])
sneezes = 0
while(m != 0):
    if m%2 == 0:
        m = m//2
    else:
        m -= 1
        sneezes += 1
print(sneezes)