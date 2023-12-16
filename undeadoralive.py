user_input = input()
count_smiley = user_input.count(':)')
count_frown = user_input.count(':(')
if count_smiley != 0 and count_frown == 0:
    print('alive')
elif count_smiley == 0 and count_frown != 0:
    print('undead')
elif count_smiley != 0 and count_frown != 0:
    print('double agent')
else:
    print('machine')