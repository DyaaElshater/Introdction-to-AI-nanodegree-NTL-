# `grid` is defined in the test code scope as the following:
# (note: changing the value here will _not_ change the test code)
# grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
from utils import *

Input2 = '53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79'
grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'


def search(values):
    global unsolvedBoxes
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
#    unsolvedBoxes_temp = values.copy()
    unsolvedBoxes_temp = {k:values[k] for k in values if len(values[k])>1}
    unsolvedBoxes= unsolvedBoxes_temp.copy()
    values = reduce_puzzle(values)
    if values is False or len ([v for v in values if len(values[v])==0])>0:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(unsolvedBoxes[s]), s) for s in unsolvedBoxes if len(unsolvedBoxes[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        unsolvedBoxes[s]=value
        attempt = search(new_sudoku)
        if attempt:
            return attempt
        else :
            unsolvedBoxes = unsolvedBoxes_temp.copy()
    
    
GrdiValueOutput = grid_values(grid2)
#print("==============================================================================================")    
#print("==============================================================================================")    

#display(GrdiValueOutput)
GrdiValueOutput = only_choice(GrdiValueOutput)    
#print("==============================================================================================")    
#print("==============================================================================================")    

#display(GrdiValueOutput)
GrdiValueOutput = reduce_puzzle(GrdiValueOutput)    
#print("==============================================================================================")    
#print("==============================================================================================")    
#display(GrdiValueOutput)
#print("==============================================================================================")    
#print("==============================================================================================")    


GrdiValueOutput = search(GrdiValueOutput)        
display(GrdiValueOutput)

"""
aa = {'A1': '4', 'A2': '1679', 'A3': '12679', 'A4': '139', 'A5': '2369', 'A6': '1269', 'A7': '8', 'A8': '1239', 'A9': '5', 'B1': '26789', 'B2': '3', 'B3': '1256789', 'B4': '14589', 'B5': '24569', 'B6': '1245689', 'B7': '12679', 'B8': '1249', 'B9': '124679', 'C1': '2689', 'C2': '15689', 'C3': '125689', 'C4': '7', 'C5': '234569', 'C6': '1245689', 'C7': '12369', 'C8': '12349', 'C9': '123469', 'D1': '3789', 'D2': '2', 'D3': '135789', 'D4': '3459', 'D5': '34579', 'D6': '4579', 'D7': '13579', 'D8': '6', 'D9': '13789', 'E1': '3679', 'E2': '15679', 'E3': '135679', 'E4': '359', 'E5': '8', 'E6': '25679', 'E7': '4', 'E8': '12359', 'E9': '12379', 'F1': '36789', 'F2': '456789', 'F3': '356789', 'F4': '3459', 'F5': '1', 'F6': '245679', 'F7': '23579', 'F8': '23589', 'F9': '23789', 'G1': '289', 'G2': '8', 'G3': '289', 'G4': '6', 'G5': '459', 'G6': '3', 'G7': '1259', 'G8': '7', 'G9': '12489', 'H1': '5', 'H2': '6789', 'H3': '36789', 'H4': '2', 'H5': '479', 'H6': '14789', 'H7': '1369', 'H8': '13489', 'H9': '134689', 'I1': '1', 'I2': '6789', 'I3': '4', 'I4': '589', 'I5': '579', 'I6': '5789', 'I7': '23569', 'I8': '23589', 'I9': '23689'}
ab = {'A1': '4', 'A2': '1679', 'A3': '12679', 'A4': '139', 'A5': '2369', 'A6': '1269', 'A7': '8', 'A8': '1239', 'A9': '5', 'B1': '26789', 'B2': '3', 'B3': '1256789', 'B4': '14589', 'B5': '24569', 'B6': '1245689', 'B7': '12679', 'B8': '1249', 'B9': '124679', 'C1': '2689', 'C2': '1569', 'C3': '125689', 'C4': '7', 'C5': '234569', 'C6': '1245689', 'C7': '12369', 'C8': '12349', 'C9': '123469', 'D1': '3789', 'D2': '2', 'D3': '135789', 'D4': '3459', 'D5': '34579', 'D6': '4579', 'D7': '13579', 'D8': '6', 'D9': '13789', 'E1': '3679', 'E2': '15679', 'E3': '135679', 'E4': '359', 'E5': '8', 'E6': '25679', 'E7': '4', 'E8': '12359', 'E9': '12379', 'F1': '36789', 'F2': '45679', 'F3': '356789', 'F4': '3459', 'F5': '1', 'F6': '245679', 'F7': '23579', 'F8': '23589', 'F9': '23789', 'G1': '29', 'G2': '8', 'G3': '29', 'G4': '6', 'G5': '459', 'G6': '3', 'G7': '1259', 'G8': '7', 'G9': '1249', 'H1': '5', 'H2': '679', 'H3': '3679', 'H4': '2', 'H5': '479', 'H6': '14789', 'H7': '1369', 'H8': '13489', 'H9': '134689', 'I1': '1', 'I2': '679', 'I3': '4', 'I4': '589', 'I5': '579', 'I6': '5789', 'I7': '23569', 'I8': '23589', 'I9': '23689'}

if(aa==ab):
    print("True ...")
else :
    print("False ...")


da = dict(zip(["one","two","three"],['123','321','555']))
db = dict(zip(["one","two","three"],['123','321','555']))


print(da==db)
"""
