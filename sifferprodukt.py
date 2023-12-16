user_input = input()
while len(user_input) > 1:
    num = 1
    for i in range(len(user_input)):
        if int(user_input[i]) != 0:
            num *= int(user_input[i])
    user_input = str(num)
print(int(user_input))