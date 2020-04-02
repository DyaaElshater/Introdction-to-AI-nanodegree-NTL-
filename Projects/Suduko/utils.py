import stdin
rows='ABCDEFGHI'
cols='123456789'
Input = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

unsolvedBoxes=dict()

def cross(a,b):
	return [s+t for s in a for t in b]

boxes = cross(rows,cols)
row_units 		= [cross(r, cols) for r in rows]
column_units  	= [cross(rows,c) for c in cols]

square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return





arrNumbers = ['1','2','3','4','5','6','7','8','9']

arrCheckCols = ['A','B','C','D','E','F','G','H','I']
def Check_Rows(grid,point):
    for PointCheckIndex in range(1,10):
        gridElement = grid.get(point[0]+str(PointCheckIndex))
        for rowIndex in range(0,9):
            if(gridElement==arrNumbers[rowIndex]):
                arrNumbers[rowIndex]='0'

def Check_Cols(grid,point):
    for PointCheckIndex in arrCheckCols:
        gridElement = grid.get(PointCheckIndex+point[1])
        for rowIndex in range(0,9):
            if(gridElement==arrNumbers[rowIndex]):
                arrNumbers[rowIndex]='0'

def Check_Squares(grid,point):
    pointCheck=''
    if(point[0]=='B' or point[0]=='C'):
        pointCheck+='A'
    elif (point[0]=='E' or point[0]=='F'):
        pointCheck+='D'
    elif (point[0]=='H' or point[0]=='I'):
        pointCheck+='G' 
    else :
        pointCheck+=point[0]     
    
    if(point[1]=='2' or point[1]=='3'):
        pointCheck+='1'
    elif(point[1]=='5' or point[1]=='6'):
        pointCheck+='4'    
    elif(point[1]=='8' or point[1]=='9'):
        pointCheck+='7'    
    else:
        pointCheck+=point[1]
    
    for SquareRowIndex in range(ord(pointCheck[1]),ord(pointCheck[1])+3):
        for SquareColIndexquare in range(ord(pointCheck[0]),ord(pointCheck[0])+3):
            gridElement=grid.get(chr(SquareColIndexquare)+chr(SquareRowIndex))
            for rowIndex in range(0,9):
                if(gridElement==arrNumbers[rowIndex]):
                    arrNumbers[rowIndex]='0'
            
def grid_values(grid):
    if len(grid) != 81:
        print("Grid must be 81 length")
    else:
        zip_data = zip(boxes,grid)
        my_grid = dict(zip_data)
        for box in my_grid :
            if my_grid.get(box) == '.':
                point=''
                Check_Rows(my_grid,box)
                Check_Cols(my_grid,box)
                Check_Squares(my_grid,box)
                for arrNumberIndex in range (0,9):
                    if (arrNumbers[arrNumberIndex]!='0'):
                        point+=str(arrNumbers[arrNumberIndex])
                    arrNumbers[arrNumberIndex]=str(arrNumberIndex+1)
                my_grid[box]=point
                unsolvedBoxes[box]=point
        return my_grid


def only_choice(values):
    Removed = []
    for box in unsolvedBoxes :      # box to another
        elementIndex=0
        for elementIndex in range (0,len(values[box])): #element to another
            flag = 0
            
            for boxescheck in peers[box]:   # search box to another
                if boxescheck in unsolvedBoxes:
                    if values[box][elementIndex] in values[boxescheck]:
                        flag=1
                        break
    
            if (flag==1):
                flag =0
                continue
            else :
                values[box]= values[box][elementIndex]
                Removed.append(box)
                break
    for RemovedBox in Removed:            
        del unsolvedBoxes[RemovedBox ]
    return values

    
def reduce_puzzle(values):
    stalled = 0
    flag =0
    while (stalled == 0) :
        solved_values_before = [box for box in unsolvedBoxes if len(values[box]) == 1]
        if (len(solved_values_before)>0):
            for box in solved_values_before :
                for boxSearch in peers[box] :
                    if(values[box]  in values[boxSearch]):
                        values[boxSearch]=values[boxSearch].replace(values[box],'')
                        if boxSearch in unsolvedBoxes :
                            unsolvedBoxes[boxSearch]=unsolvedBoxes[boxSearch].replace(values[box],'')
                    else :
                        flag=1
            if (flag == 1):
                flag=0
                for deletedBox in solved_values_before:
                    del unsolvedBoxes[deletedBox]
        else:
            break
    return values