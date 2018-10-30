import mysql.connector
import jellyfish
from collections import OrderedDict
import unicodedata
from tqdm import tqdm

def formatString (list):
    formatList=[]
    list = [tuple(map(str, eachTuple)) for eachTuple in list]
    for each in list:
        each = str(each).strip("(),',""")
        each = each.lower()
        formatList.append(each)
    return formatList

def FormatStr (value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    each = value.strip("(),',""")
    each = each.lower()
    return each




cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='data_integration')
cur = cnx.cursor()

cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'imdb';")
imdb = cur.fetchall()

cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'rotten_tomatoes';")
rotten_tomatoes = cur.fetchall()

cur.execute("SELECT * FROM imdb limit 500;")
imdb_data = cur.fetchall()

cur.execute("SELECT * FROM rotten_tomatoes limit 500;")
rotten_data=cur.fetchall()

cnx.close()


imdb = formatString(imdb)
rotten_tomatoes = formatString(rotten_tomatoes)


mapping = OrderedDict()


list1=[]

for each in imdb:
    if each not in mapping:
        mapping[each] = {}
        for item in rotten_tomatoes:
            mapping[each][item]=0
            # print mapping[each]

#print mapping.keys()

print len(imdb)
for i in tqdm(range(0 , len(imdb))):
    for each in imdb_data:
        for j in range(0, len(rotten_tomatoes)):
            for item in rotten_data:
                if(type(item[j]) != int):
                    items = FormatStr(item[j])
                    neue = FormatStr(each[i])
                if(items == neue):
                    # if(rotten_tomatoes[j] in mapping[imdb[i]]):
                    mapping[imdb[i]][rotten_tomatoes[j]]= mapping[imdb[i]][rotten_tomatoes[j]]+1
                    # else:
                    #     mapping[imdb[i]]= {rotten_tomatoes[j],1}



for each in mapping.keys():
    print each, mapping[each]

# z=0
#
# list2=[]
# for x in rotten_data:
#     x = list(x)
#     list2.append(x)
#
# while(z!= len(list1)):
#     for i in range(len(list2)):
#         for j in range(len(list2[i])):
#             if(list1[z] == list2[i][j]):
#                 i=i
#                 #print list2[i][j]
#                 #print i,j
#     z=z+1
#
#

