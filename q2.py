from statistics import mean 
from itertools import islice 

s1 = input()
s2 = input().split(" ")
#s1_num = [int(x) for x in s1]
s2_num = [int(y) for y in s2]
N = int(s1[0])
K = int(s1[-1])
avg = []


for i in range(len(s2)):
    zip_list = zip(*(islice(s2_num, i, None) for j in range(i)))
    output = list(map(mean, zip_list))
    #splits = i+1
    #output = [sum(s2_num[i:i + splits])/splits 
          #for j in range(len(s2_num) - splits + 1)]
    avg.extend(output)

print(sum(m >= K for m in avg))
      
'''
count = 0
for a in range(len(avg)):
    if avg[a] >= K:
        print(len(avg) - count)
        break
    count += 1
'''
