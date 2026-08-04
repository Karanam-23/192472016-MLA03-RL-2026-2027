gamma=0.9

reward=[10,5,0]

value=[0,0,0]

for i in range(2,-1,-1):
    if i==2:
        value[i]=reward[i]
    else:
        value[i]=reward[i]+gamma*value[i+1]

print(value)
