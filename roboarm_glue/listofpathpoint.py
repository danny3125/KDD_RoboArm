import cnc_input


def A_walkonchip(matrices,gluewidth):
    allsteps = []
    for matrix in matrices:
       allsteps.extend(A_walkinmatrix(matrix[0],matrix[1],matrix[2],int(gluewidth)))                 
    return allsteps

def A_walkinmatrix(matrix,startpoint_x, startpoint_y,gluewidth ):
    walkpoints = []
    start = 1
    end = len(matrix)
    for i in range(1, len(matrix[0]),gluewidth):
        for j in range(start,end,gluewidth):
            walkpoints.append((startpoint_x + i, startpoint_y + j))
        temp = end
        end = start
        start = temp
        gluewidth = - gluewidth
    return walkpoints


def main():
    test,gluewidth = cnc_input.main(['-i','mother_board.json'])
    print(gluewidth)
    walkpoints = A_walkonchip(test,gluewidth)
    return walkpoints






if __name__ == '__main__':
    main()
