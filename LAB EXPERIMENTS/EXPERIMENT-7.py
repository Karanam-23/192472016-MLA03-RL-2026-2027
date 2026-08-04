cost=[4,2,7,3]

dp=[0]*len(cost)

dp[0]=cost[0]

for i in range(1,len(cost)):
    dp[i]=cost[i]+dp[i-1]

print(dp)
