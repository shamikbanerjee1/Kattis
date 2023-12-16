user_input = input().split('/')
a = int(user_input[0])
b = int(user_input[1])
if a > 12:
    print('EU')
elif b > 12:
    print('US')
else:
    print('either')