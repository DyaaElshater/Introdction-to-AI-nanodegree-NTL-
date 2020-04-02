
def dictAssign (source ):
    return dict(zip(source.keys(),[source[KEY]for KEY in source ]))


def rec (x):
    x['3']=100
    
      
x=dict(zip([str(z) for z in range(1,10)],[y for y in range(1,10)]))   
zz=dictAssign(x)   
rec(x)
print(zz)
print(x)




"""
def search(value):
    valueTemp = dictAssign(value)
    unSolvedLables = [s for s in value if len(value[s])!=1]
    if (len(unSolvedLables) == 0):
        print("Done")       ########################################################
        return value
    else :
        """ Getting the smallest element box """
        MinLable  = 0
        MinValue  = 0
        MinSize   = 9
        for boxLable in unSolvedLables :
            if (len(value[boxLable]) == 2):
                MinLable = boxLable
                MinValue = value[boxLable]
                break
            if (len(value[boxLable])<MinSize)       :
                MinSize  = len(value[boxLable])
                MinLable = boxLable
                MinValue = value[boxLable]
        
        """ Reduce Elements """
        print ("MinLable = "+MinLable+"\t MinValue = "+value[boxLable])######################
        global unsolvedBoxes
        unsolvedBoxesTemp = dictAssign(unsolvedBoxes)
        for element in MinValue:
            print("Element : "+element)
            value[MinLable]=element
            display(value)
            unsolvedBoxes = dictAssign(unsolvedBoxesTemp)
            unsolvedBoxes[MinLable]=element
            value2 = reduce_puzzle(value)
            print ("After reduce_puzzle")
            display(value2)
            if(value2==valueTemp):      
                print("No change")
                continue
            elif (len([newBox for newBox in value if len(value[newBox]) == 0]) >0 ):
                print("Wrong Element")
                value = dictAssign(valueTemp)
                continue
            else :
                print("Changed")
                value2 = search(value2)
                if (len([s for s in value if len(value[s])!=1])==0):
                    return value2
        return valueTemp        
"""


"""
def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        print("Solved")
        return values ## Solved!
    if (len([values[v] for v in values if len(values[v])==0])>0):
        return 0
    # Choose one of the unfilled squares with the fewest possibilities
    display (values)
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    print(s)
    
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if (attempt == 0 ):
            continue
        if attempt:
            print("Attempt :: ")
            display (attempt)
            return attempt
"""     
