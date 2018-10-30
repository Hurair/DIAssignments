import csv
from tqdm import tqdm
import re

def purify(dict):
    for each in dict:

        for idx, every in enumerate(dict[each][0]):

            if (every == "" and dict[each][1][idx] != ""):
                dict[each][0][idx] = dict[each][1][idx]

            if (idx == 7 or idx == 10):
                dict[each][0][idx] = re.sub("\D", "", dict[each][0][idx])

            if (idx == 6 and len(dict[each][0][6]) > len(dict[each][1][6])):
                dict[each][1][idx] = dict[each][0][idx]

        for idx, every in enumerate(dict[each][1]):
            if (every == "" and dict[each][0][idx] != ""):
                dict[each][1][idx] = dict[each][0][idx]

            if (idx == 7 or idx == 10):
                dict[each][1][idx] = re.sub("\D", "", dict[each][1][idx])

            if (idx == 6 and len(dict[each][1][6]) > len(dict[each][0][6])):
                dict[each][0][idx] = dict[each][1][idx]

    return dict

def search(a):
    reader = csv.reader(open('inputDB.csv', 'r'))
    for data in reader:
        if data[0] == a:
            return data

realdata=[]
reader = csv.reader(open('update.csv', 'r'))


dictf = {}
dicts = {}
i = 0
j = 0

for data in reader:
    realdata.append(data)


for idx,each in tqdm(enumerate(realdata)):
    if(idx < len(realdata)/2):
        first = []
        for every in each:
            first.append(search(every))
        dictf[i]=first
        i=i+1
    else:
        second = []
        for every in each:
            second.append(search(every))
        dicts[j] = first
        j = j + 1

print dictf
print dicts


purify(dictf)
purify(dicts)

