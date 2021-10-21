f = open('C:/Users/dtien/College/CSE373HW6TF1.txt','r')
lines = f.readlines()
edges = (lines[0])[0:len(lines[0])-1]   #String of number of edges
vertices = (lines[1])[0:len(lines[1])-1]    #String of number of vertices
#Every other line is a connection
#print(lines)    #Print out our lists of strings
#print(edges)    #Print out how many edges we have
#print(vertices) #Print out how many vertices we have

edgesList = (lines)[2:len(lines)]
#print("Edges: \n", edgesList)#Prints out all connections

list1 = [0] * int(vertices)
count = 1

for x in range(int(vertices)):
    list1[x] = count
    count = count + 1
#Instantiates each index with its appropriate value
    
#print(list1)

matrix1 = [[]] * int(vertices)
#print(matrix1)  #Blank matrix of appropriate length instantiated

count = 1
for row in range(len(matrix1)):
    matrix1[row] = [count]
    count = count + 1
#print("Base: \n", matrix1)  #Matrix with appropriate rows instantiated

for x in edgesList: #Goes through every connection from textfile
    if edgesList.index(x)!=(len(edgesList)-1): x = x[0:len(x)-1]   
    #print("Bridge: ", x)    #Prints out particular connection separated by space
    vertex1 = x[0:x.find(' ')]  #String representation of starting vertex
    vertex2 = x[x.find(' ')+1:len(x)] #Representation of ending vertex
    vertex1 = int(vertex1)  #Turns into integer
    vertex2 = int(vertex2)  #Turns into integer
    #print(vertex1)  #Prints out vertex1 value
   # print(vertex2)  #Prints out vertex2 value
    matrix1[vertex1-1].append(vertex2)
    matrix1[vertex2-1].append(vertex1)
    
#print("Connections: \n", matrix1)  #All connections between each edge for each vertex established

for entry in matrix1:
    #print(entry)
    index = matrix1.index(entry)
    for value in entry:
        #print("Value:")
        #print(value)
        #print("Entry")
        #print(entry)
        #print("Addition")
        #print(matrix1[value-1])
        #print(entry + matrix1[value-1])
        if entry!=matrix1[value-1]:
            for integer in matrix1[value-1]:
                if integer not in entry: entry.append(integer)
        if entry!=matrix1[value-1]:
            matrix1[value-1] = []
        entry = matrix1[index]
#print(matrix1, '\n')  #Complete list with some empty sets

finalList = []

for entry in matrix1:
    if entry != []: finalList.append(entry)
#Creates final list that's trimmed of empty sets
    
#print(finalList)
componentNumber = 1
for components in finalList:
    print("Connected Component #", componentNumber, ': \n', components)
    componentNumber = componentNumber+1
#Prints output for all connected components
