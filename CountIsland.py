import random

def CountIsland(map):
    #Define Answer as 0 (not found any island)
    found = 0

    #Get number of row and column
    rows = len(map)
    cols = len(map[0])

    #Define seen as 2D list for recheck which coordinate was visited, default is 0 mean not visit yet, 1 mean visited
    seen = [[0 for x in range(cols)] for y in range(rows)]

    #Define direction as dir for easily usgage when do BFS contain E W N S
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    #Nested loop for traverse in 2D list use rows and cols
    for i in range(rows):
        for j in range(cols):
            
            #Boolen statement when we found any land if found land mean found an island
            if map[i][j] and not seen[i][j]:
                
                seen[i][j] = 1
                found += 1
                
                #Define stack for store land coordinate also use queue or normal list will work fine
                stack = [(i, j)]
                
                #Do Breadth first search : Search for any land that connect to each other one by one
                #This process will do untill stack is empty (noo more land connected)
                while len(stack):
                    #Extract last coordinate that was stored x y will be use as flag for search four direction 
                    x, y = stack.pop()
                    
                    #This loop for look at four directions E W N S
                    for sub_dir in dir:
                        
                        #Boolean statement for check if new coordinate was not out of range or visited
                        #List seen was use for not to re-submit a visited coordinate if not it can cause infinite loop
                        if (x + sub_dir[0] >= 0 and x + sub_dir[0] < rows and y + sub_dir[1] >= 0 and y + sub_dir[1] < cols and not seen[x + sub_dir[0]][y + sub_dir[1]] and map[x + sub_dir[0]][y + sub_dir[1]]):
                            
                            #If boolean statement was true than register new coordinate in seen as 1 and append into stack for next search coordinate
                            seen[x + sub_dir[0]][y + sub_dir[1]] = 1
                            stack.append((x + sub_dir[0], y + sub_dir[1]))
                            
            #Base case if it 0 alway register as visited 
            else:
                seen[i][j] = 1

    return found
#============================ Test Space ===============================#

def genranInt(max, min = 1):
    return random.randint(min, max)

def genTestcase(max_row, max_cols):
    rows = genranInt(max_row)
    cols = genranInt(max_cols)
    
    map = [[0 for x in range(cols)] for y in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if genranInt(10) > 5:
                map[i][j] = 1
    return map

def DisplayMap(map):
    for rows in map:
        print(rows)

map01 = [[1, 0, 0, 1], 
         [0, 1, 1, 1], 
         [0, 0, 0, 1], 
         [0, 1, 0, 1]]

map02 = [[1, 0, 1, 0], 
         [0, 1, 0, 1], 
         [1, 0, 1, 0], 
         [0, 1, 0, 1]]

map03 = [[1, 0, 1, 0, 0 ,1, 0,1,1,1,1,1,1,1,0]] 

map04 = genTestcase(5,10)


def RunTestcase(map):
    print("========================= Test map =========================")
    DisplayMap(map)
    print('\n' + "======================= Island found =======================")
    print(CountIsland(map))

RunTestcase(map04)