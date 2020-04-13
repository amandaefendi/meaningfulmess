#====================================================================
# Took extracts from
# https://code.activestate.com/recipes/119466-dijkstras-algorithm-for-shortest-paths/
# for Dijkstra()
#====================================================================


#
# functionsD.py : functions used in part 4
#

import re
from DSAGraph import *

def askFilename():
    """Ask user to enter which marginal file they want to use."""
#    print("\nDo you have the file already?"+
#          "\nYes - proceed\t\t No - go back to main menu")
#    choice = input("(Y/N)   ")
#    if choice.upper() == "N":
#        filename = None
#    elif choice.upper() == "Y": 
    print("\nInsert file name (without the filetype)")
    print("(PRESS CTRL+C IF THERE IS NO FILE YET!!)")
    fileOpt = input("or press enter if saved on default name:   ") 
    if fileOpt != "":
        filename = fileOpt+".txt"
    else:
        print("\n\nFinding file...")
        print("\n\nWhich party is it for?")
        print("A. Labor\t\t B. Liberal")
        partyOpt = input("Selected party is (A/B):  ")
        list1 = ["A", "B"]
        while partyOpt.upper() not in list1:
            partyOpt = input("Selected party is (A/B):  ")
        marginOpt = input("\nWhat was the margin used? (enter as int)   ")
        if partyOpt.upper() == "A":
            filename = "LaborParty_MarginalSeatList"+str(marginOpt)+"%.txt"
        elif partyOpt.upper() == "B":
            filename = "LiberalParty_MarginalSeatList"+str(marginOpt)+"%.txt"
    return filename


def readInputFile(marginalFile):
    """Reading input marginal file.

    Keyword arguments:
    marginalFile -- exported txt file of the marginal seats
    """
    marginRegex = re.compile(r'''
        (\D+)				#divname
        (\s)
        (\D+)				#state
        (\:\s)                          #(: )
        (\-?\d{1}\.?\d+)                #-d.dddddddddd
        ''', re.VERBOSE)

    matchlist = []

    for line in marginalFile[2::]:
        line = line.strip()
        match = marginRegex.search(line)
        if match:
            matchlist.extend([match.group(1), match.group(3)])
    return matchlist


def convertTravelTime(traveltime):
    """Convert time in hours and minutes to minutes.

    Keyword arguments:
    traveltime -- travel time in hours and minutes
    """
    hour = traveltime[0]
    minute = traveltime[2:4]
    minutes = int(hour)*60 + int(minute)
    return minutes


def insertAirport(airport, matchlist):
    """Adding airports to the graph.

    Keyword arguments:
    airport -- list of data from the airport csv
    matchlist -- list of marginal division
    """
    graph = DSAGraph()
    for i in range(1,len(airport)):
        if airport[i][10] == "plane":
            From = airport[i][1]
            To = airport[i][5]
            weight = convertTravelTime(airport[i][9]) 
            importToGraph(graph, From, To, weight, matchlist)
    return graph


def insertElect(graph, elect, matchlist):
    """Adding divisions in elect to the graph.

    Keyword arguments:
    graph -- graph object
    elect -- list of data from the csv file
    matchlist -- list of marginal division
    """
    for i in range(1,len(elect)):
        From = elect[i][1]
        To = elect[i][5]
        weight = int(elect[i][9])/60    #from seconds to minutes
        importToGraph(graph, From, To, weight, matchlist)
    return graph


def importToGraph(graph, From, To, weight, matchlist):
    """Adding vertices and edges to graph.

    Keyword arguments:
    graph -- graph object
    From -- label of source division
    To -- label of destination division
    weight -- travel time in minutes between
    matchlist -- list of marginal divisions
    """
    #if both source and destination are not in the graph
    if graph.findVertex(From)==None and graph.findVertex(To)==None:
        graph.addVertex(From)
        graph.addVertex(To)
        graph.addEdge(From, To, weight)

    #if source is already in the graph, but not destination
    elif graph.findVertex(From)!=None and graph.findVertex(To)==None:
        graph.addVertex(To)
        graph.addEdge(From, To, weight)

    #if destination is already in the graph, but not source
    elif graph.findVertex(From)==None and graph.findVertex(To)!=None:
        graph.addVertex(From)
        graph.addEdge(From, To, weight)

    #if both source and destination are already in the graph
    else:
        graph.addEdge(From, To, weight)

#MIGHT TAKE OFF VERTEX.MARGINAL OFF JUST TBH -.-
#MATCH THE MARGINAL USING THE REGEX LIST 
#MATCH AGAINST DIJKSTRA RESULTS AND LOOKUP PATH


def setDistanceInf(graph, D):
    """Setting dictionary values as inifinty.

    Keyword arguments:
    graph -- graph object
    D -- dictionary for total distance
    """
    for i in graph.vertices:
        D[i] = float('inf')
#        print("set distance infinity to "+i)
    return D


#do shotest path of first div in marginallist
#examine output path, run for loop and match each against all marginal

def Dijkstra(graph, start, end=None):
    """Find shortest path?
    
    Keyword arguments:
    graph -- graph object
    start -- starting node
    end -- NOT destination node BUT end of graph node
    """
    graph.clearVisited()
    D = {}		#dictionary of final distances
    P = {}		#dictionary of previous vertices
    D = setDistanceInf(graph, D)	#initial distance is infinity
    D[start] = 0	#total distance from start to start is 0
    

    #start from vertex with label: start
    v = start #this is also curNode's label

    #while is not the last vertex unvisited
    while v != None:

        #go to vertex with label v set is as current
        curNode = graph.findVertex(v)

        #set currentNode as visited
        curNode.visited = True
        w = curNode.label		#w (string) is where we are now

        #see all neighbours of curNode
        curEdges = curNode.links	#LL of adjacent vertices
        edge = iter(curEdges)		#iterator of curEdges is edge

        for i in range(curEdges.size):
            a = next(edge)

            #curNode's neighbour is called v
            v = a.divName		#name of adjacent division
#            print('\n'+'next neighbour is '+v)
#            print(graph.findVertex(v))
            if graph.findVertex(v).visited == False:
#                print("\ncurrently in: "+w)
#                print("looking at neighbour: "+v)           
    
                #distance from start to vertex v
                #a.data: btwn curNd and neighbour
                #D[w]: distance from start to curNd
                totalDist = int(a.data)+int(D[w])
                if totalDist < D[v]:
                    D[v] = totalDist 	#replace dist to dict with key:v
#                    print("travel time from "+start+" to "+v+" is "+str(totalDist))
                    P[v] = w 
#                    print("Added to "+v+"'s path: "+w)

        #after all neighbours have been checked
	#find the closest neighbour of curNode(v)
        nextMin = curNode.data.peekMin() #see heap's root: closest neighbour
        nextMinNode = graph.findVertex(nextMin)
        nextMinLab = nextMinNode.label
#        print("nextmin is "+nextMinLab)

	#if closest neighbour is alr visited
        while nextMinNode.visited == True:	
#            print("nextmin is visited")
            nextMinNode1 = curNode.data.nextMin(nextMinNode.label) #next closest 

	    #heap.nextMin()
            #return none is end of heap is reached
            #no more neighbours to visit
            if nextMinNode1 == None:
#                print("NEXT MIN IS NONE")
                nextMinLab = None
                break
            else:
#                print("nextMin is : "+nextMinNode1)
                nextMinNode = graph.findVertex(nextMinNode1)
                nextMinLab = nextMinNode.label
        #found the next closest and not visited
        #take the label name as v
        
        v = nextMinLab
#        print("minNode is "+v)

    return (D,P)


def findAirport(state):
    """Gives corresponding airport name for each state."""
    if state == "NSW":
        airport = "Sydney Airport"
    elif state == "VIC":
        airport = "Melbourne Airport"
    elif state == "QLD":
        airport = "Brisbane Airport"
    elif state == "TAS":
        airport = "Hobart Airport"
    elif state == "WA":
        airport = "Perth Airport"
    elif state == "SA":
        airport = "Adelaide Airport"
    elif state == "NT":
        airport = "Darwin Airport"
    return airport
   
       
def makePath(P, path, src, dst):
    """Trace back shortest path and display.

    Keyword arguments:
    P -- dictionary containing vertices from Dijkstra
    path -- stack object
    src -- start journey from this division
    dst -- destination is this division
    """
    print("Path from "+src+" to "+dst)
    previousV = P[dst]
    while previousV != src:
        path.push(previousV)
        temp = previousV
        previousV = P[temp]
    path.push(previousV)
    for i in range(path.getCount()):
        print(path.pop())



