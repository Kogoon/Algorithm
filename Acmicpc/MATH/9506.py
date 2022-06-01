import sys
input = sys.stdin.readline

while True:
    a = []
    
    n = int(input())
    
    if n == -1:
        sys.exit()

    for i in range(1, n//2+1):
        if n%i == 0:
            a.append(i)

    temp = sum(a)
    if temp == n:
        print(f'{n} = ', end="")
        for i in a:
            if i == a[-1]:
                print(i, end="")
            else: 
                print(i, end=" ")
                print("+ ", end="")
        print(end='\n')
    else:
        print(f'{n} is NOT perfect.')
