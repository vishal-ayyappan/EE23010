import numpy as np

m = 1000
count1=0
count2=0
for i in range(m):
    rs1=np.random.randint(1,75)
    count1+=1
    if rs1 in range(1,65):
        count2+=1
prob1=count2/count1
print(1-prob1)

