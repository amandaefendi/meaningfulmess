#
# functionsB.py : containing all functions used in part B
#

from DSATrees import *
from DSAQueue import *

def BfilterMenu():
    """Display options for filter in part B."""
    print("\nDisplay filter by:")
    print("A. State\t\t B. Party")
    filterOpt = input("Selected filter is (A/B):  ")
    return filterOpt.upper()


def insert_bySTATE(state, data):
    """Insert matched rows by state into BST and adding
    an inner list of details into each node.

    Keyword arguments:
    state -- chosen state
    data -- list of data from csv
    """
    i = 1
    BT = DSABinaryTrees()
    while i != len(data):
        if data[i][0] == state:
            inKey = data[i][6]+" "+data[i][7]
            BT.insert(inKey, data[i][5])           #key is Fullname, value is ID
            curNode = BT.find(inKey, BT.root)
            for n in range(len(data[i])-1, -1, -1):
                curNode.details.append(data[i][n])
        i = i + 1
    return BT

def insert_byPARTY(party, data):
    """Insert matched rows by party into BST.

    Keyword arguments:
    party -- chosen party
    data -- list of data
    """
    i = 0
    BT = DSABinaryTrees()
    if party == "A":
        party = "LP"
    elif party == "B":
        party = "ALP"
    elif party == "C":
        party = "GRN"
    elif party == "D":
        party = "NP"
    while i != len(data):
        if data[i][3] == party:              #row i col 4 (partyNm)
            inKey = data[i][6]+" "+data[i][7]
            BT.insert(inKey, data[i][4])     #key=inKey, value=PartyName
            curNode = BT.find(inKey, BT.root)
#            print(curNode.getKey())
            for n in range(len(data[i])-1, -1, -1):
#                print(data[i][n])
                curNode.details.append(data[i][n])
        i = i + 1
    return BT


def display_matchedInput(BT, input1):
    """Match user input with ListNode data.

    Keyword arguments:
    input1 -- user input
    BT -- binary tree of names and details
    """
    curNode = BT.find(input1, BT.root)                  #get matched node to curNode
    try:
        outputQ = DSAQueue()
        while curNode != None:
            details = curNode.details
            printDetails(details)
            #Queue is for writing file purposes
            outputQ.enqueue(details)
            curNode = BT.find(input1, curNode._rightChild)
    except MissingKeyTreeError as error:
        print(error)
    return outputQ


def printDetails(details):
    """Display details for a ListNode.

    Keyword arguments:
    details -- list of details of a list node
    """
    print("\nMATCH FOUND\tState: "+details[9])
    print("Full name    : "+ details[2]+" "+details[3])
    print("Candidate ID : "+details[4])
    print("Party name   : "+details[5])
    print("Division     : "+details[7]+"\n")


def BfileWriteout(outputQ, filename):
    """Write results into a txt file.

    Keyword arguments:
    outputQ -- queue of list of details
    filename -- name of file to be written
    """
    filename1 = filename + ".txt"
    f = open(filename1, "w+")
    for i in range(outputQ.getCount()):
        person = outputQ.dequeue()
        print(person)
        f.write("\nState: "+person[9]+"\n"+
            "Full name    : "+ person[2]+" "+person[3]+"\n"
            "Candidate ID : "+person[4]+"\n"+
            "Party name   : "+person[5]+"\n"+
            "Division     : "+person[7]+"\n")
    f.close()
