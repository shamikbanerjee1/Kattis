def calculate_years(P,R,F):
    years = 0
    while True:
        if P<=F:
            P*=R
            years+=1
        else:
            break
    return years
T = int(input())
for _ in range(T):
    P,R,F = map(int, input().split())
    years = calculate_years(P,R,F)
    print(years)
