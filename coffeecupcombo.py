lectures = int(input())
coffee_list = input()
max_lectures_awake = 0
max_coffee_carried = 0
for i in range(lectures):
    if int(coffee_list[i]) == 1:
        max_lectures_awake += 1
        if max_coffee_carried == 0:
            max_coffee_carried += 2
        elif max_coffee_carried == 1:
            max_coffee_carried += 1
    else:
        if max_coffee_carried > 0:
            max_lectures_awake += 1
            max_coffee_carried -= 1
print(max_lectures_awake)