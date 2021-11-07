import csv
import numpy 
import pandas as pd
from sklearn.decomposition import NMF

ingredients = []
nameset = set()

data = []
cat = []

with open(r'C:\Users\DHYHZ\Desktop\nbtrial\ingredientsv3.csv') as f:
    row1 = csv.reader(f)
    counter = 1
    for rec in row1:
        #print(counter)
        if rec != []:# and rec[1] == "":
            if rec[0][-1] == ' ':
                if rec[1] != '1':
                    nameset.add(rec[0][:-1])
            else:
                if rec[1] != '1':
                    nameset.add(rec[0])
        counter += 1
    for i in sorted(nameset):
        ingredients.append(i)
    #print(len(ingredients))
        
with open(r'C:\Users\DHYHZ\Desktop\nbtrial\drugdatav3.csv') as g:
    row4 = csv.reader(g)
    for entry in row4:
        if entry[0] not in data:
                data.append(entry[0])
            
dataset = numpy.zeros(shape=(len(data),len(ingredients)))

df = pd.DataFrame(dataset,
                       columns = ingredients,
                       index = data
                       )



with open(r'C:\Users\DHYHZ\Desktop\nbtrial\drugdatav3.csv') as h:
    row3 = csv.reader(h)
    for entry in row3:
        if entry[2] != "1":
            df.loc[entry[0]][entry[1]] = 1
            if entry[4] != '':
                if entry[4] == "Coatings":
                    cat.append(1)
                elif entry[4] == "Granules":
                    cat.append(2)
                elif entry[4] == "Semi-solids":
                    cat.append(3)
                elif entry[4] == "Solutions/Suspensions":
                    cat.append(4)
                elif entry[4] == "Tablet":
                    cat.append(5)

df.to_csv(r'C:\Users\DHYHZ\Desktop\nbtrial\excipient_matrixv1.csv')

prediction = pd.read_csv(r'C:\Users\DHYHZ\Desktop\nbtrial\excipient_matrix_test.csv', index_col = 0)


for i in range(1,141): 
    print(i)
    model = NMF(n_components=i, init='random', random_state=0, max_iter=160000)
    W = model.fit_transform(prediction)
    H = model.components_
    #print(i)
    #print(W)
    #print(H)
    a = numpy.array(W)
    b = numpy.array(H)
    vv = numpy.matmul(a, b)
    #print(a.shape)
    #print(b.shape)
    #print(vv.shape)
    #print(" ")
    pd.DataFrame(vv,
                 columns = ingredients,
                 index = data
                 ).to_csv(r'C:\Users\DHYHZ\Desktop\nbtrial\predictions_test\{name}.csv'.format(name=i))
"""
model = NMF(init='random', random_state=0, max_iter=400)
W = model.fit_transform(df)
H = model.components_
print(W)
print(H)
a = numpy.array(W)
b = numpy.array(H)
vv = numpy.matmul(a, b)
"""

