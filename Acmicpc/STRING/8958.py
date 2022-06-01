import sys 
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a = list(input().strip())
    temp = 0
    count = 0
    for i in a:
        if i == 'O':
            temp += 1
            count += temp
        elif i == 'X':
            temp = 0

    print(count)
            
