import cnc_input
import json
import matplotlib.pyplot as plt


def A_walkonchip(matrices):
    allsteps = []
    for matrix in matrices:
       allsteps.extend((sides_in_matrix(matrix[0],matrix[1],matrix[2])))
    return allsteps

def sides_in_matrix(matrix,startpoint_x, startpoint_y ):
    sides_of_matrix = ((startpoint_x,startpoint_y),(startpoint_x + len(matrix),startpoint_y)\
    ,(startpoint_x,startpoint_y + len(matrix[0]),(startpoint_x + len(matrix),startpoint_y + len(matrix[0]))))
    '''
    for i in range(1, len(matrix),6):
        for j in range(1,len(matrix[0]),6):
            walkpoints.append((startpoint_x + i, startpoint_y + j))
    return walkpoints'''
    return sides_of_matrix
    
test = cnc_input.main(['-i','right_chip.json'])
print(test[2][0])
plt.imshow(test[6][0], cmap = plt.get_cmap('gray'))
A_walkonchip(test)