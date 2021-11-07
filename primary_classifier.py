import csv
import numpy
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier

#drugnames = []
ingredients = []
nameset = set()
gnb = 0
bnb = 0
mnb = 0
nnc = 0
nnc1 = 0
rfc = 0

tabs = 0
sols = 0
gels = 0
coat = 0
gran = 0

with open(r'C:\Users\DHYHZ\Desktop\nbtrial\ingredients_list_pri_class.csv') as f:
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

for rd in range(1,5):
    train = []
    test = []

    train_cat = []
    test_cat = []

    train_set = set()
    test_set = set()

    with open(r'C:\Users\DHYHZ\Desktop\nbtrial\drug_data_primary_classification.csv.csv') as g:
        row4 = csv.reader(g)
        for entry in row4:
            if entry[5] == str(rd):
                test_set.add(entry[0])
                if entry[0] not in test:
                    test.append(entry[0])
            else:
                train_set.add(entry[0])
                if entry[0] not in train:
                    train.append(entry[0])
                

        
    train_matrix = numpy.zeros(shape=(len(train_set),len(ingredients)))       
    test_matrix = numpy.zeros(shape=(len(test_set),len(ingredients)))

    train_matrix_df = pd.DataFrame(train_matrix,
                           columns = ingredients,
                           index = train
                           )

    test_matrix_df = pd.DataFrame(test_matrix,
                           columns = ingredients,
                           index = test
                           )

    #matrix_df.to_csv(r'C:\Users\DHYHZ\Desktop\matrix_df.csv')

    with open(r'C:\Users\DHYHZ\Desktop\nbtrial\drugdatav2.csv') as h:
        row3 = csv.reader(h)
        for entry in row3:
            
            if entry[5] == str(rd):
                test_matrix_df.loc[entry[0]][entry[1]] = 1
            
                if entry[4] != '':
                    if entry[4] == "Coatings":
                        test_cat.append(1)
                        coat += 1
                    elif entry[4] == "Granules":
                        test_cat.append(2)
                        gran += 1
                    elif entry[4] == "Semi-solids":
                        test_cat.append(3)
                        gels += 1
                    elif entry[4] == "Solutions/Suspensions":
                        test_cat.append(4)
                        sols += 1
                    elif entry[4] == "Tablet":
                        test_cat.append(5)
                        tabs += 1
                        
            else:
                train_matrix_df.loc[entry[0]][entry[1]] = 1
            
                if entry[4] != '':
                    if entry[4] == "Coatings":
                        train_cat.append(1)
                        coat += 1
                    elif entry[4] == "Granules":
                        train_cat.append(2)
                        gran += 1
                    elif entry[4] == "Semi-solids":
                        train_cat.append(3)
                        gels += 1
                    elif entry[4] == "Solutions/Suspensions":
                        train_cat.append(4)
                        sols += 1
                    elif entry[4] == "Tablet":
                        train_cat.append(5)
                        tabs += 1

    #train_matrix_df.to_csv(r'C:\Users\DHYHZ\Desktop\nbtrial\train_matrix_df.csv')
    #test_matrix_df.to_csv(r'C:\Users\DHYHZ\Desktop\nbtrial\test_matrix_df.csv')

    #with open(r'C:\Users\DHYHZ\Desktop\nbtrial\excset.csv', 'w') as a:
    #    writer = csv.writer(a, lineterminator = '\n')
    #    for i in ingredients:
    #        writer.writerow([i])
            

    #with open(r'C:\Users\DHYHZ\Desktop\nbtrial\test_cat.csv', 'w') as b:
    #    writer = csv.writer(b, lineterminator = '\n')
    #    writer.writerow(test_cat)  

    print(rd)  
    clf_NB = GaussianNB()
    clf_NB.fit(train_matrix_df, train_cat)
    gnb += clf_NB.score(test_matrix_df, test_cat)
    print(clf_NB.score(test_matrix_df, test_cat))

    clf_Bernoulli = BernoulliNB()
    clf_Bernoulli.fit(train_matrix_df, train_cat)
    bnb += clf_Bernoulli.score(test_matrix_df, test_cat)
    print(clf_Bernoulli.score(test_matrix_df, test_cat))

    clf_Multinomial = MultinomialNB()
    clf_Multinomial.fit(train_matrix_df, train_cat)
    mnb += clf_Multinomial.score(test_matrix_df, test_cat)
    print(clf_Multinomial.score(test_matrix_df, test_cat))

    

    clf = MLPClassifier(hidden_layer_sizes=(100,50,), random_state=1, max_iter=300).fit(train_matrix_df, train_cat)
    #print(clf.predict_proba(train_matrix_df))

    clf.predict(test_matrix_df)
    nnc += clf.score(test_matrix_df, test_cat)
    print(clf.score(test_matrix_df, test_cat))

    clf1 = MLPClassifier(hidden_layer_sizes=(100,50,), solver = 'sgd', random_state=1, max_iter=3000).fit(train_matrix_df, train_cat)
    #print(clf.predict_proba(train_matrix_df))

    clf1.predict(test_matrix_df)
    nnc1 += clf1.score(test_matrix_df, test_cat)
    print(clf1.score(test_matrix_df, test_cat))


    clf_rf = RandomForestClassifier(max_depth=3, random_state=0)
    clf_rf.fit(train_matrix_df, train_cat)
    rfc += clf_rf.score(test_matrix_df, test_cat)
    #print(clf_rf.score(test_matrix_df, test_cat))
    #print(clf_rf.get_params())

print("Averages:")
print(" ")
print("Naive Bayes")
print(gnb/4)
print("Bernoulli Naive Bayes")
print(bnb/4)
print("Mutinomial Naive Bayes")
print(mnb/4)
print("Neural Network")
print(nnc/4)
print("Neural Network sgd")
print(nnc1/4)
#print("Random Forest")
#print(rfc/4)
print(sols/4)
print(tabs/4)
print(gels/4)
print(gran/4)
print(coat/4)

