t = int(input())
    
for i in range(1,t+1):
    A, B=map(int,input().split())
    print("Case #%d: %d + %d = %d" % (i, A, B, A+B))