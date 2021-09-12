import sys 
input = sys.stdin.readline

def fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    return fibo(num-1) + fibo(num-2)

T = int(input())   # Test case
fibo_data = [0, 1]
zero_data = [1, 0]
one_data = [0, 1]

for _ in range(T): # 'T' times
    num = int(input())
    
    if num == 0:
        print('{} {}'.format(zero_data[num], one_data[num]))
    elif num == 1:
        print('{} {}'.format(zero_data[num], one_data[num]))
    else:
        for i in range(2, num+1):
            fibo_data.append(fibo_data[i-1]+fibo_data[i-2])
            zero_data.append(zero_data[i-1]+zero_data[i-2])
            one_data.append(one_data[i-1]+one_data[i-2])
        print('{} {}'.format(zero_data[i], one_data[i]))
