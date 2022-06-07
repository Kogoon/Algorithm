"""
INPUT
2
8 1
1 4
5 4
7 5
5 8
3 7
6 5
2 6
1 0 0 1 1 0 0 1
5 6
1 2
2 3
3 4
4 5
1 0 1 1 0

OUTPUT
#1 12
#2 15
"""
import sys
input = sys.stdin.readline


def main():
    T = int(input())

    for i in range(T):
        N, K = map(int, input().split())
    
        graph = [[] for p in range(N+1)]
        
        for j in range(N-1):
            x, y = map(int, input().split())
            graph[x].append(y)
            graph[y].append(x)
            
        #print(graph)
    
        criminal = list(input().split())
        criminal_count = 0
        for k in range(len(criminal)):
            criminal[k] = int(criminal[k])
            if criminal[k] == 1:
                criminal_count += 1
                
        #print(criminal)
        #print(criminal_count)
        
        if K >= N:
            print("#{} {}".format(i+1, N*criminal_count))
            continue
    
        count = 0
    
        for l in range(1, N+1):
            if criminal[l-1] == 1:
                count += 1
            for m in range(len(graph[l])):
                temp = graph[l][m] - 1
                if criminal[temp] == 1:
                    count += 1
                
        print("#{} {}".format(i+1, count))


if __name__ == '__main__':
    main()
        
            
            
        
