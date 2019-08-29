N=int(input())
n1=list(map(int,input().split()))
min,max=map(int,input().split())
for i in range(N):
	if(min==n1[i]):
		while(n1[i]!==max):
			count++
			i++

print(count)
