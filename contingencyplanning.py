from math import factorial
n = int(input())
y = sum(list(map(lambda x: factorial(n)//factorial(n-x),[i for i in range(1,n+1)])))
print('JUST RUN!!') if y>10**9 else print(y)