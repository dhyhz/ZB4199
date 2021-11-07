import csv
import numpy
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

#drugnames = []
ingredients = []
nameset = set()

data = []
cat = []

with open(r'C:\Users\DHYHZ\Desktop\nbtrial\ingredients.csv') as f:
    row1 = csv.reader(f)
    counter = 1
    for rec in row1:
        #print(counter)
        if rec != []:# and rec[1] == "":
            if rec[0][-1] == ' ':
                nameset.add(rec[0][:-1])
            else:
                nameset.add(rec[0])
        counter += 1
    for i in sorted(nameset):
        ingredients.append(i)

#print(len(drugnames))
#print(len(ingredients))

with open(r'C:\Users\DHYHZ\Desktop\nbtrial\drugdatav2.csv') as g:
    row4 = csv.reader(g)
    for entry in row4:
        if entry[0] not in data:
                data.append(entry[0])
            
dataset = numpy.zeros(shape=(len(data),len(ingredients)))

df = pd.DataFrame(dataset,
                       columns = ingredients,
                       index = data
                       )



with open(r'C:\Users\DHYHZ\Desktop\nbtrial\drugdatav2.csv') as h:
    row3 = csv.reader(h)
    for entry in row3:
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
                    
df.to_csv(r'C:\Users\DHYHZ\Desktop\nbtrial\matrix_df.csv')

df_train, df_test, cat_train, cat_test = train_test_split(df, cat, test_size=0.25, random_state=1)

#with open(r'C:\Users\DHYHZ\Desktop\nbtrial\train_cat.csv', 'w') as a:
#    writer = csv.writer(a, lineterminator = '\n')
#    writer.writerow(train_cat)
        

#with open(r'C:\Users\DHYHZ\Desktop\nbtrial\test_cat.csv', 'w') as b:
#    writer = csv.writer(b, lineterminator = '\n')
#    writer.writerow(test_cat)  
  
clf_NB = GaussianNB()
clf_NB.fit(df_train, cat_train)
print(clf_NB.score(df_test, cat_test))

clf_Bernoulli = BernoulliNB()
clf_Bernoulli.fit(df_train, cat_train)
print(clf_Bernoulli.score(df_test, cat_test))

clf_Multinomial = MultinomialNB()
clf_Multinomial.fit(df_train, cat_train)
print(clf_Multinomial.score(df_test, cat_test))

from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(random_state=1, max_iter=300).fit(df_train, cat_train)
#print(clf.predict_proba(train_matrix_df))

clf.predict(df_test)

print(clf.score(df_test, cat_test))

from sklearn.ensemble import RandomForestClassifier

clf_rf = RandomForestClassifier(max_depth=3, random_state=0)
clf_rf.fit(df_train, cat_train)
print(clf_rf.score(df_test, cat_test))
#print(clf_rf.get_params())
