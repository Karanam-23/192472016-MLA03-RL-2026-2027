import random

epsilon=0.2

ads=[0,0]

reward=[0,0]

for i in range(20):

    if random.random()<epsilon:
        arm=random.randint(0,1)
    else:
        arm=reward.index(max(reward))

    r=random.randint(0,10)

    reward[arm]+=r

print(reward)
