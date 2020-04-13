#
# C-Functions.py : functions used in part C, displaying marginal seats
#
#import pandas as pd
import string
from DSATrees import *
from DSAStack import *
from DSALinkedList import *

#===============================================================================


def listDivisions_byState(dataL):  #filename):
    """Making a list of divisions within one State.

    Keyword arguments:
    dataL -- list containing csv data for one state
    """
#    DF = pd.read_csv(filename)
#    divisions = DF['DivisionNm'].unique()
    BT = DSABinaryTrees()
    for i in range(1, len(dataL)):
        inKey = dataL[i][2]
        try:
             BT.insert(inKey, dataL[i][1])
        except DuplicateKeyError as error:
            pass
    q = BT.inorderTraverse(BT.root, BT.size)
    divisions = []
    for i in range(q.getCount()):
        divisions.append(q.dequeue())      
    return divisions

def calculateMargin(dataL, party, divisionList, m=6):
    """Calculate margin percentage per division in one state

    Keyword arguments:
    dataL -- list containing csv data for one state
    party -- chosen party by user input
    divisionList -- list of divisions in the state
    m -- default marginal threshold set as 6
    """
    voteFor = 0
    voteAgainst = 0
    n = 0
    marginal = DSALinkedList()		

    for i in range(2, len(dataL)-1):

        if dataL[i][2] == dataL[i+1][2]:

            #if still within the same division
            if dataL[i][11] == party:
                voteFor = voteFor + int(dataL[i][13])
            elif dataL[i][11] != party:
                voteAgainst = voteAgainst + int(dataL[i][13])

        elif dataL[i][2] != dataL[i+1][2]:

            #if all entries for one division is already saved
            divisionName = divisionList[n]+" "+dataL[1][0]
            n = n + 1
            percentage = str((voteFor / (voteFor + voteAgainst))*100)+"%"
            margin = float((voteFor / (voteFor + voteAgainst))*100 - 50)
            if margin < m and margin > -m:
                marginal.insertLast(divisionName, margin)
                print(divisionName+" "+str(margin))
            voteFor = 0
            voteAgainst = 0        
    
    print(marginal.getSize())
    return marginal   
        

def CfileWriteout(filename, linkedlist):
    """Appending results from linkedlist to a txt file.

    Keyword arguments:
    filename -- name of txt file
    linkedlist -- LL of marginal seats in a state
    """
    f = open(filename, "a+")
    a = iter(linkedlist)
    try:
        n = linkedlist.getSize()
        for i in range(n):
            curNode = next(a)
            write = str(curNode.divName)+": "+str(curNode.data)+"\n"
            f.write(write)
        f.close()
    except StopIteration as error:
        print(error)

