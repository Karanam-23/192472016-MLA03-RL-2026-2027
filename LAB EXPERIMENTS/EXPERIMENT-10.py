episodes=10

returns=[]

for i in range(episodes):

    reward=0

    for j in range(5):
        reward+=1

    returns.append(reward)

print(sum(returns)/episodes)
