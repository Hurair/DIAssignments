
from itertools import product
import jellyfish
from tqdm import tqdm

with open("inputDB.csv") as inputFile:
    aList = inputFile.read().split("\n")

    aProduct = product(aList,aList)
# with open('update.csv', 'w') as outFile:
    for aElem,bElem in tqdm(aProduct):
        if ( aElem != bElem and jellyfish.jaro_distance(unicode(aElem, "utf-8"), unicode(bElem, "utf-8")) > 0.90):
            list1 = aElem.split(",")
            list2 = bElem.split(",")
            output = list1[0]+ "," +list2[0]+"\n"
            # outFile.write(output)
