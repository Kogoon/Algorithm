import sys 
input = sys.stdin.readline

T = int(input())   # Test case
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
            zero_data.append(zero_data[i-1]+zero_data[i-2])
            one_data.append(one_data[i-1]+one_data[i-2])
        print('{} {}'.format(zero_data[num], one_data[num]))
