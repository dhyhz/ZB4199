import csv
import numpy
import pandas as pd

#drugnames = []
categories = {}
names = []
num = []
ingredients = []
nameset = set()


with open(r'C:\Users\DHYHZ\Desktop\nbtrial\split.csv') as f:
    row1 = csv.reader(f)
    counter = 0
    for rec in row1:
        if counter%2 == 0:
            names.append(rec[0])
        else:
            num.append(rec[0])
        counter += 1

    for i in range(len(names)):
        categories[names[i]] = num[i]
with open(r'C:\Users\DHYHZ\Desktop\nbtrial\ingredients.csv') as f:
    row3 = csv.reader(f)
    counter = 1
    for rec in row3:
        #print(counter)
        if rec != []:# and rec[1] == "":
            if rec[0][-1] == ' ':
                ingredients.append(rec[0][:-1])
            else:
                ingredients.append(rec[0])
        counter += 1
        
with open(r'C:\Users\DHYHZ\Desktop\nbtrial\ingredients.csv') as f:
    row2 = csv.reader(f)
    counter = 1
    categorised_df = pd.DataFrame(row2)
    c = 0
    for i in range(len(categorised_df)):
        if categorised_df.loc[i][0][-1] == ' ':
            if categorised_df.loc[i][1] == '':
                categorised_df.loc[i][1] = categories[categorised_df.loc[i][0][:-1]]
        else:
            if categorised_df.loc[i][1] == '':
                categorised_df.loc[i][1] = categories[categorised_df.loc[i][0]]
        c += 1
        #print(c)

categorised_df.to_csv(r'C:\Users\DHYHZ\Desktop\nbtrial\ing_cat_df.csv')

#with open(r'C:\Users\DHYHZ\Desktop\nbtrial\test_cat.csv', 'w') as b:
#    writer = csv.writer(b, lineterminator = '\n')
#    writer.writerow(test_cat)  
  

