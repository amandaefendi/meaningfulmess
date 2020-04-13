#
# mains.py : containing the main menu system
#

from functionsB import *
from functionsC import *
from functionsD import * 
from DSATrees import *
#from DSALinkedList import *
#from DSAQueue import *
import math
import re
#import string
#import pandas as pd

# Opening File for Task1 and Task2 ===========================================================

with open('HouseCandidatesDownload-20499.csv') as fileobj:
    csvdata = fileobj.read().splitlines()
data = []
for line in csvdata:
    splitline = line.split(',')
    data.append(splitline)

# Opening File for Task3  ====================================================================

def openFile(filename): 
    """Read csv and replace dodgy stuff.

    Keyword arguments:
    filename -- csv file name
    """
    find = '"Shooters, Fishers and Farmers"'
    replace = 'Shooters Fishers and Farmers'
    datalist = []
    with open(filename) as fileobj1:
        csvdata1 = fileobj1.read().splitlines()
    for line in csvdata1:
        line = str.replace(line, find, replace)
        splitline = line.split(',')
        datalist.append(splitline)
    return datalist

act = openFile("PrefbyPP-ACT.csv")
nsw = openFile("PrefbyPP-NSW.csv")
vic = openFile("PrefbyPP-VIC.csv")
qld = openFile("PrefbyPP-QLD.csv")
tas = openFile("PrefbyPP-TAS.csv")
wa = openFile("PrefbyPP-WA.csv")
sa = openFile("PrefbyPP-SA.csv")
nt = openFile("PrefbyPP-NT.csv")

# Opening File for Task4 =====================================================================

with open('AirportDist1.0.csv') as fileobj:
    csvdata = fileobj.read().splitlines()
airport = []
for line in csvdata:
    splitline = line.split(',')
    airport.append(splitline)

with open('ElectDist1.1.csv') as fileobj:
    csvdata = fileobj.read().splitlines()
elect = []
for line in csvdata:
    splitline = line.split(',')
    elect.append(splitline)


print("\nFILE OPENED\n")

#Non-TaskSpecific Functions ===================================================================


def mainMenu():
    """Display of main options."""
    print("\n----------------------------------------------------------------")
    print("\t\t\t MAIN MENU")
    print("----------------------------------------------------------------")
    print("\nWhat would you like to do today?")
    print("\tA. List of nominee")
    print("\tB. Nominee search")
    print("\tC. List by margin")
    print("\tD. Itinerary by margin")
    print("\t-- Press Enter to quit")

def displayState():
    """Displays all the states"""
    print("\nWhat state would you like?")
    print("A. ACT\t\t E. TAS")
    print("B. NSW\t\t F. WA")
    print("C. VIC\t\t G. SA")
    print("D. QLD\t\t H. NT")

def displayParty():
    """Displays all the parties."""
    print("\nWhich party would you like?")
    print("A. Liberal\t\t C. The Greens")
    print("B. Labor\t\t D. The Nationals")

def takeFilter():
    """Takes user's filter option between state or party."""
    print("\nFilter by:")
    print("A. State\t\t B. Party")
    filterOpt = input("Selected filter is (A/B):  ")
    list1 = ["A", "B"]
    while filterOpt.upper() not in list1:
        filterOpt = input("Selected filter is (A/B):   ")
    return filterOpt.upper()

def ask_toWriteFile():
    writeFile = input("\nWould you like to save report to a file? (Y/N)    ")
    list1 = ["Y", "N"]
    while writeFile.upper() not in list1:
        writeFile = input("Would you like to save report to a file? (Y/N)    ")
    if writeFile.upper() == "Y":
        ret = True
    elif writeFile.upper() == "N":
        ret = False
    return ret


#Function for option  A. LIST OF CANDIDATES ================================================


def AfilterMenu():
    """Display of filter options, take order option and insert to tree."""
    filterOpt = takeFilter()
    if filterOpt.upper() == "A":
        displayState()
        stateOpt = input("Selected state (ACT/NSW/VIC/etc):  ")
        list1 = ["ACT", "NSW", "VIC", "QLD", "TAS", "WA", "SA", "NT"]
        while stateOpt.upper() not in list1:
            stateOpt = input("Selected state (ACT/NSW/VIC/etc):  ")
        orderOpt = AorderMenu()
        insertTreeSTATE(stateOpt.upper(), orderOpt.upper())
    elif filterOpt.upper() == "B":
        displayParty()
        partyOpt = input("Selected party is (A-D):  ")
        list1 = ["A", "B", "C", "D"]
        while partyOpt.upper() not in list1:
            partyOpt = input("Selected party is (A-D):  ")
        insertTreePARTY(partyOpt.upper())	#argument only filter, order is only A
                

def AorderMenu():
    """Display of order (sort by) options."""
    print("\nOrder by:")
    print("A. Surname\nB. Party")
    orderOpt = input("Selected order is (A-B):   ")
    list1 = ["A", "B"]
    while orderOpt.upper() not in list1:
        orderOpt = input("Selected order is (A-B):   ")
    return orderOpt.upper()


def insertTreeSTATE(state, order):
    """Inserting items by state to a Binary Tree and preorder display.

    Keyword arguments:
    state -- chosen state
    order -- chosen order (sort by)
    """
    if order == "A":
        #order by surname this will be the key value for BT
        i = 0
        size = 0
        BT = DSABinaryTrees()
        while i != len(data):
            if data[i][0] == state:        #row i col 0 (stateAb)
                inKey = data[i][6]+" "+data[i][7]
                BT.insert(inKey, data[i][4]) #key=inKey, value=PartyName
                size = size + 1
            i = i + 1
        q = BT.inorderTraverse(BT.root, size)
        print("\n----------------------------------------------------------------")
        print("\nList of Candidates, filtered by State and ordered by Surname\n")
        a = iter(q.queue)
        try:
            n = q.queue.getSize()
            for i in range(n):
                curNode = next(a)
                print(curNode.divName)
        except StopIteration as error:
            print(error)
        print("\n----------------------------------------------------------------")

        #Ask to write file
        writefile = ask_toWriteFile()    
        if writefile == True:
            print("\n\t\tFile Written")
            filename = "ACandidateList-bySTATE"+state+"ordbySURNAME"
            AfileWriteout(q, filename)
   
    elif order == "B":
        #FITLER BY STATE ORDER BY PARTYNAME
        i = 0
        size = 0
        BT = DSABinaryTrees()
        while i != len(data):
            if data[i][0] == state:
                inKey = data[i][4]+"\t| "+data[i][6]+" "+data[i][7]
                #inKey is "partyName | Fullname" to avoid double key
                BT.insert(inKey, data[i][7]) #inValue is firstname (?)
                size = size + 1
            i = i + 1
        q = BT.inorderTraverse(BT.root, size)
        print("\n----------------------------------------------------------------")
        print("\nList of Candidates, filtered by State and ordered by Party\n")
        a = iter(q.queue)
        try:
            n = q.queue.getSize()
            for i in range(n):
                curNode = next(a)
                print(curNode.divName)
        except StopIteration as error:
            print(error)
        print("\n----------------------------------------------------------------")
        
        #Ask to write file
        writefile = ask_toWriteFile()    
        if writefile == True:
            print("\n\t\tFile Written")
            filename = "ACandidateList-bySTATE"+state+"ordbyPARTY"
            AfileWriteout(q, filename)


def insertTreePARTY(party):
    """Inserting items by party to a Binary Tree and preorder display.

    Keyword arguments:
    party -- chosen party
    order -- order is default by surname
    """
    #PARTY FILTER SURNAME(DEFAULT) ORDER
    i = 0
    size = 0
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
            size = size + 1
        i = i + 1
    q = BT.inorderTraverse(BT.root, size)
    print("\n----------------------------------------------------------------")
    print("\n\tList of Candidates, filtered by Party and ordered by Surname")
    print("\tPARTY NAME: "+party+"\n")
    a = iter(q.queue)
    try:
        n = q.queue.getSize()
        for i in range(n):
            curNode = next(a)
            print(curNode.divName)
    except StopIteration as error:
        print(error)
    print("\n----------------------------------------------------------------")

    #Ask to write file
    writefile = ask_toWriteFile()    
    if writefile == True:
        print("\n\t\tFile Written")
        filename = "ACandidateList-byPARTY"+party+"ordbySURNAME"
        AfileWriteout(q, filename)


def AfileWriteout(q, filename):
    """Write results into a txt file.

    Keyword arguments:
    q -- output queue used for display
    filename -- name of file to be written
    """
    filename1 = filename + ".txt"
    f = open(filename1, "w+")
    f.write(str(filename)+"\n\n")
    f.close()
    f = open(filename1, "a+")
    a = iter(q.queue)
    try:
        n = q.queue.getSize()
        for i in range(n):
            curNode = next(a)
            f.write(curNode.divName+"\n")
        f.close()
    except StopIteration as error:
        print(error)
    



# MENU STARTS HERE ============================================================


mainMenu()
choice = input("Your Selection is (A-D):\t")

while choice.upper() != "":

    if choice.upper() == "A":

        print("\n----------------------------------------------------------------")
        print("\n\n\t\t\tLIST OF NOMINEES")
        #Takes filter opt, order opt, read file insert to tree, and display preorder xD
        #Save report to file or not?
        AfilterMenu()	

        #Ask if want to display more?
        again = input("\n\nWould you like to display more? (Y/N): ")
        while again.upper() != "N" and again.upper() == "Y":
            AfilterMenu()
            again = input("\n\nWould you like to display more? (Y/N): ")

    elif choice.upper() == "B":

        print("\n----------------------------------------------------------------")
        print("\n\n\t\t\tNOMINEE SEARCH")
        filterOpt = BfilterMenu()               #A is state filter, B is party filter
        if filterOpt.upper() == "A":

            #Selecting filter and initialising BST
            displayState()
            stateOpt = input("Selected state (ACT/NSW/VIC/etc):  ")
            list1 = ["ACT", "NSW", "VIC", "QLD", "TAS", "WA", "SA", "NT"]
            while stateOpt.upper() not in list1:
                stateOpt = input("Selected state (ACT/NSW/VIC/etc):  ")
            binaryTree = insert_bySTATE(stateOpt.upper(), data)
            
            #Begin taking input, match and display
            print("\nSearching process:")
            substring = input("Enter substring of surname...  ")
            while substring == "":
                print("\n\t\tSubstring can not be empty. Try again.\n")
                substring = input("Enter substring of surname...  ")
            try:
                foundNode = binaryTree.find(substring.upper(), binaryTree.root)		
                q = display_matchedInput(binaryTree, substring.upper())
            except MissingKeyTreeError as error:
                print("\n\t\tNo match found.")
                print(error)
            #if all entries for one division is already saved

           #Ask if user wants to write out report to file
            writefile = ask_toWriteFile()    
            if writefile == True:
                print("\n\t\tFile Written")
                filename = "BCandidateList-bySTATE"+stateOpt.upper()+"by"+substring.upper()
                BfileWriteout(q, filename)
            

        elif filterOpt.upper() == "B":
            
            #Selecting filter and initialising BST
            displayParty()
            partyOpt = input("Selected party is (A-D):  ")
            list1 = ["A", "B", "C", "D"]
            while partyOpt.upper() not in list1:
                partyOpt = input("Selected party is (A-D):  ")
            binaryTree = insert_byPARTY(partyOpt.upper(), data)    

            #Begin taking input, match and display
            print("\nSearching process:")
            substring = input("Enter substring of surname...  ")
            while substring == "":
                print("\n\t\tSubstring can not be empty. Try again.\n")
                substring = input("Enter substring of surname...  ")
            try:
                foundNode = binaryTree.find(substring.upper(), binaryTree.root)
                q = display_matchedInput(binaryTree, substring.upper())
                print(q.getCount())
            except MissingKeyTreeError as error:
                print("\n\t\tNo match found.")
                print(error)

           #Ask if user wants to write out report to file
            writefile = ask_toWriteFile()    
            if writefile == True:
                print("\n\t\tFile Written")
                filename = "BCandidateList-byPARTY"+partyOpt.upper()+"by"+substring.upper()
                BfileWriteout(q, filename)


    elif choice.upper() == "C":

        #Displaying options for state
        print("\n----------------------------------------------------------------")
        print("\n\t\tCALCULATING MARGINAL SEATS BY PARTY")
        print("\n\nWhich party would you like?")
        print("A. Labor\t\t B. Liberal")
        partyOpt = input("Selected party is (A/B):  ")
        list1 = ["A", "B"]
        while partyOpt.upper() not in list1:
            partyOpt = input("Selected party is (A/B):  ")
        if partyOpt.upper() == "A":
            party = ["ALP", "LaborParty"]
        elif partyOpt.upper() == "B":
            party = ["LP", "LiberalParty"]

        #Ask for custom margin
        print("\n\nWould you like a custom margin? (default is 6%)")
        marginOpt = input("Insert as integer or press enter \t")
        if marginOpt == "":
            m = 6
        else:
            while marginOpt.isdigit == False: #while not empty string (enter)
                marginOpt = input("Insert as integer or press enter \t")
            m = int(marginOpt)
        print("\nCalulating votes...\n")        

        #Calculating votes and margin through all states
        ACT_divList = listDivisions_byState(act)
        ACT_marginal = calculateMargin(act, party[0], ACT_divList, m)
        print("ACT DONE (margin "+str(m)+"%)\n")
        NSW_divList = listDivisions_byState(nsw)
        NSW_marginal = calculateMargin(nsw, party[0], NSW_divList, m)
        print("NSW DONE (margin "+str(m)+"%)\n")
        VIC_divList = listDivisions_byState(vic)
        VIC_marginal = calculateMargin(vic, party[0], VIC_divList, m)
        print("VIC DONE (margin "+str(m)+"%)\n")
        QLD_divList = listDivisions_byState(qld)
        QLD_marginal = calculateMargin(qld, party[0], QLD_divList, m)
        print("QLD DONE (margin "+str(m)+"%)\n")
        TAS_divList = listDivisions_byState(tas)
        TAS_marginal = calculateMargin(tas, party[0], TAS_divList, m)
        print("TAS DONE (margin "+str(m)+"%)\n")
        WA_divList = listDivisions_byState(wa)
        WA_marginal = calculateMargin(wa, party[0], WA_divList, m)
        print("WA DONE (margin "+str(m)+"%)\n")
        SA_divList = listDivisions_byState(sa)
        SA_marginal = calculateMargin(sa, party[0], SA_divList, m)
        print("SA DONE (margin "+str(m)+"%)\n")
        NT_divList = listDivisions_byState(nt)
        NT_marginal = calculateMargin(nt, party[0], NT_divList, m)
        print("NT DONE (margin "+str(m)+"%)\n")

        #Option to write to file
        writeout = input("\nWould you like to save results to a txt file? Y/N   ")
        if writeout.upper() == "Y":
            customName = input("\nEnter name of output file without filetype"+
                               "\n(or press enter for default):   ")
            if customName == '':
                filename1 = party[1]+"_MarginalSeatList"+str(m)+"%.txt"
            else:
                filename1 = customName+".txt"
            f = open(filename1, "w+")
            f.write("List of Marginal Seats of "+party[1]+" in Australia\n"+
                    "Margin used: "+str(m)+"%\n\n")
            f.close()
            CfileWriteout(filename1, ACT_marginal)
            CfileWriteout(filename1, NSW_marginal)
            CfileWriteout(filename1, VIC_marginal)
            CfileWriteout(filename1, QLD_marginal)
            CfileWriteout(filename1, TAS_marginal)
            CfileWriteout(filename1, WA_marginal)
            CfileWriteout(filename1, SA_marginal)
            CfileWriteout(filename1, NT_marginal)
    

    elif choice.upper() == "D":

        #ask what marginal to refer to?
        print("\n----------------------------------------------------------------")
        print("\n\t\tITINERARY BASED ON MARGINAL SEATS")
        print("\nTo create itinerary, you must have an existing marginal"
              +"\nseat file saved for a certain party and certain margin.")
        #try to find file and use exception if not found
        while True:
            filename = askFilename()
            print("filename is:"+filename)
            try:
                fileobj = open(filename)
                marginal = fileobj.readlines()
            except OSError as error:
                print(error.errno)
            else:
                break
            print("out of while")

        #process the txt file using regex
        marginList = readInputFile(marginal)       

        #all airports connect to other airports
        #make the graph, connect the airports
        #loc is for locations (so it makes sense :D )
        loc = insertAirport(airport, marginList)        

        #read from elect and add to graph
        loc = insertElect(loc, elect, marginList)

        #erm do i BFS now??????????
        #use dijkstra
        #only take to and from nodes that are in marginList`
        minutes = 0
        for i in range(0,len(marginList),2):
            src = marginList[i]
            if int(i)+2 > len(marginList)-1:
                break
            dst = marginList[i+2]
            D,P = Dijkstra(loc,src)
            print("\n\n\n\n================================================================")
            print("Path from "+src+" to "+dst)
            path = DSAStack()

            try:
                previousV = P[dst]
            except KeyError as error:		#need to change state
                print("\n\t==Must go to airport first!==\n")
                tempSrc = marginList[i+1]	#currentState airport
                tempDst = marginList[i+3]	#destState airport
                srcAirport = findAirport(tempSrc)
                dstAirport = findAirport(tempDst)
                #Div to airport
                makePath(P,path, src, srcAirport)
                print(srcAirport)
                print("Total time taken for trip is: "+str(D[srcAirport])+"\n")
                minutes = minutes + D[srcAirport]
                #Airport to Airport
                makePath(P,path, srcAirport, dstAirport)
                print(dstAirport)
                print("Total time taken for trip is: "+str(D[dstAirport])+"\n")
                minutes = minutes + D[dstAirport]
                #Airport to Division
                src = dstAirport
                D,P = Dijkstra(loc, src)

            makePath(P, path, src, dst)
            print(dst)
            print("Total time taken for trip is: "+str(D[dst])+"\n")
            minutes = minutes + D[dst]
        print("\n\nTotal travel time accross all marginal division: "+str(minutes)+" minutes\n")

    #when each option has been executed, show main menu again
    mainMenu()
    choice = input("Your Selection is (A-D):\t")


