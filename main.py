import os, time
 
def getListOfFilesDirectories(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFilesDirectories(fullPath) #recurrency nice
        else:
            allFiles.append(fullPath)                
    return allFiles  

listOfIdeaProjects = os.listdir('C:/Users/BRITENET/IdeaProjects')

print('Choose ideaProject: ')
i = 1
projectsMap = {}
for elem in listOfIdeaProjects:
    print(str(i) + '. ' + str(elem))
    projectsMap[str(i)] = elem
    i = i + 1


choice = input()
dirName = "C:/Users/BRITENET/IdeaProjects/" + str(projectsMap[choice]) + "/src"

listOfFiles = getListOfFilesDirectories(dirName)
print('Deployed file(s):                [simply lastModifiedDate != createdDate]')
i = 1
for elem in listOfFiles:
    if (time.ctime(os.path.getmtime(elem)) != time.ctime(os.path.getctime(elem))) and not str(elem).endswith("xml") : 
        elem = str(elem)
        print(str(i) + '. ' + elem[elem.rindex("\\") + 1 : len(elem) ])
        i = i + 1 

input()
 
