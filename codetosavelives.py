testcases = int(input())
for i in range(testcases):
    user_input1 = int(''.join(input().split()))
    user_input2 = int(''.join(input().split()))
    res = str(user_input1 + user_input2)
    for i in range(len(res)):
        print(res[i],end = ' ')
    print()