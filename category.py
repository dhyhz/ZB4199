import csv
import numpy
import pandas as pd

arr = []
excipients = set()
active = []

antiadherents = [] #2
binders = [] #3
coatings = [] #4
colours = [] #5
disintergrants = [] #6
flavours = [] #7
gildants = [] #8
lubricants = [] #9
preservatives = [] #10
sorbents = [] #11
sweeteners = [] #12
vehicles = [] #13


with open(r'C:\Users\DHYHZ\Desktop\nbtrial\ingredients.csv') as f:
    row1 = csv.reader(f)
    counter = 1
    for rec in row1:
        #print(counter)
        if rec != []:# and rec[1] == "":
            if rec[1] == '1':
                if rec[0][-1] == ' ':
                    active.append(rec[0][:-1])
                else:
                    active.append(rec[0])
            else:
                if rec[0][-1] == ' ':
                    excipients.add(rec[0][:-1])
                else:
                    excipients.add(rec[0])
        counter += 1

#print(len(drugnames))
#print(len(ingredients))
"""
for excipient in excipients:
    print(excipient)
    category = input()
    if category == '0':
        antiadherents.append(excipient)
    elif category == '1':
        binders.append(excipient)
    elif category == '2':
        coatings.append(excipient)
    elif category == '3':
        colours.append(excipient)
    elif category == '4':
        disintergrants.append(excipient)
    elif category == '5':
        flavours.append(excipient)
    elif category == '6':
        gildants.append(excipient)
    elif category == '7':
        lubricants.append(excipient)
    elif category == '8':
        preservatives.append(excipient)
    elif category == '9':
        sorbents.append(excipient)
    elif category == '10':
        sweeteners.append(excipient)
    elif category == '11':
        vehicles.append(excipient)
    elif category =='a':
        active.append(excipient)
           
"""
    
matrix = numpy.zeros(shape=(len(excipients),1))       

excipients_df = pd.DataFrame(matrix, columns = ["category"], index = excipients)

for excipient in excipients:
    if excipient in antiadherents:
        excipients_df.loc[excipient]["category"] = 2
    elif excipient in binders:
        excipients_df.loc[excipient]["category"] = 4
    elif excipient in colours:
        excipients_df.loc[excipient]["category"] = 5
    elif excipient in disintergrants:
        excipients_df.loc[excipient]["category"] = 6
    elif excipient in flavours:
        excipients_df.loc[excipient]["category"] = 7
    elif excipient in gildants:
        excipients_df.loc[excipient]["category"] = 8
    elif excipient in lubricants:
        excipients_df.loc[excipient]["category"] = 9
    elif excipient in preservatives:
        excipients_df.loc[excipient]["category"] = 10
    elif excipient in sorbents:
        excipients_df.loc[excipient]["category"] = 11
    elif excipient in sweeteners:
        excipients_df.loc[excipient]["category"] = 12
    elif excipient in vehicles:
        excipients_df.loc[excipient]["category"] = 13
    elif excipient in coatings:
        excipients_df.loc[excipient]["category"] = 3

excipients_df.to_csv(r'C:\Users\DHYHZ\Desktop\excipients_df.csv')
        


