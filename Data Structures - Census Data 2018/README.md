# Create Data Structures to Store and Process Census Data

## Tasks
1. Build a suitable data structure for effective storage and display (upon query) of candidate profiles
2. Implement filtering and search
3. Calculate and display suburbs that have marginal preferrence for each candidate
4. Make a campaign route to all the marginal areas (bonus points if shortest-path algorithm is implemented)

#### Contents:
- mains.py		- where all the codes are
- functionsB.py		- functions specific for task 2
- functionsC.py		- functions specific for task 3
- functionsD.py		- functions specific for task 4

#### Files from other pracs:
- DSATrees.py		: used on part A and B (mainly)
- DSAQueue.py		: used in DSATrees Preorder Display
- DSALinkedList.py	: used for part C to store marginal divisions and the margins
- DSAGraph.py		: used for part D to store locations and run traversal
- DSAStack.py		: used for part D to diplay shortest path
- DSAHeaps.py		: used for part D's traversal to maintain priority for min values

#### TEST HARNESSES:
- testDSATrees -> testing for DSATrees.py
- testDSAHeaps -> testing for DSAHeaps.py
- testDSAStack -> testing for DSAStack.py
- testDSAQueue -> testing for DSAQueue.py
- testFunctionsD.py -> testing for DSAGraph.py, DSALinkedList.py  AND functionsD.py

### Notes for testFunctionsD.py:
mainly a test harness for dijkstra in functionsD.py to thoroughly check Dijkstra's workflow:
please unhash the print statements in functionsD's Dijkstra()

### Notes on datasets:
List of candidates by name:
- firstly edited by vim 181006
- used 'dd' to delete the first row of the header





#### HOW TO RUN MAINS.PY

#### part A:
1. select filter between state or party
2. enter selected state by abbreviation!
3. example: WA  not by A.WA -> A
4. enter selected party by option
5. then select sort by surname or party
6. may save file depending on input
7. and can choose to display more or exit to main menu

#### part B:
1. select filter between state or party
2. then enter substring
3. once list is displayed
4. may save file depending on input
5. goes back to main menu

#### part C:
1. select which party Labor or Liberal
2. then enter margin, can be custom margin or just press enter for default
3. after list of divisions are displayed
4. may save file depending on input
5. file can be saved as a custom name
6. or choose default filename format

#### part D:
*[IMPORTANT] should do part C before part D*
- part D assumes that user already have a file to process
- if file on part C is saved on custom name: 
  - user must precisely enter the filename without .txt
- if file on part C is saved on default format: 
  - user must follow prompts, if file is not found, exception will ask user to enter again*
- once file is found:
  - the code does its magic and will display the shortest path from each division in the list to other divisions down the list

*[IN CASE CODE CRASHES*] if the code doesn't work:
make sure to save marginal list from part C 
for: Labor and 3% margin
then run the Part D code again to see results
(I tested part D with Labour and 3% margin, so at least it should work)

there is no save file option for part D :(

