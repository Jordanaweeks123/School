import math
#  File: Spiral.py

#  Description: This creates a spiral given a dimension then gives a 3x3 subset of values based around an input value.

#  Student's Name: Jordan Weeks

#  Student's UT EID: jaw6235

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number: 50295

#  Date Created: 2/15/2020

#  Date Last Modified: 2/17/2020


#  Input: dim is a positive odd integer
#  Output: function returns a 2-D list of integers arranged
#          in a spiral
def create_spiral (dim):
    spiral_grid = []
    if dim % 2 != 0:
        dim_y = dim - 1
        dim_x = dim - 1
        for i in range(dim):
            spiral_grid.append([])
            for j in range(dim):
                spiral_grid[i].append('')
        dim_sqr = dim ** 2
    else:
        dim_y = dim
        dim_x = dim
        if dim % 2 == 0:
            dim_y = dim
            dim_x = dim
            for i in range(dim+1):
                spiral_grid.append([])
                for j in range(dim+1):
                    spiral_grid[i].append('')
            dim_sqr = (dim+1) ** 2
    dim_y = int((dim)/2)
    dim_x = int((dim)/2)
    middle = [dim_x, dim_y]
    ctr = 1
    num_moves = 1
    spiral_grid[middle[0]][middle[1]] = ctr
    while ctr < dim_sqr:
        if ctr % 2 != 0:
            middle[1] += 1
            ctr += 1
            spiral_grid[middle[0]][middle[1]] = ctr
            for i in range(num_moves):
                ctr += 1
                middle[0] += 1
                spiral_grid[middle[0]][middle[1]] = ctr
            for i in range(num_moves):
                ctr += 1
                middle[1] -= 1
                spiral_grid[middle[0]][middle[1]] = ctr
        else:
            middle[1] -= 1
            ctr += 1
            spiral_grid[middle[0]][middle[1]] = ctr
            for i in range(num_moves):
                ctr += 1
                middle[0] -= 1
                spiral_grid[middle[0]][middle[1]] = ctr
            for i in range(num_moves):
                ctr += 1
                middle[1] += 1
                spiral_grid[middle[0]][middle[1]] = ctr
        num_moves += 1
    return (spiral_grid)


#  Input: grid a 2-D list containing a spiral of numbers
#         val is a number withing the range of numbers in
#         the grid
#  Output: sub-grid surrounding the parameter val in the grid
#          sub-grid could be 1-D or 2-D list
def sub_grid (grid, val):
    if val > len(grid)**2:
        print('Number not in Range')
        return
    else:
        s_grid = []
        for i in range(3):
            s_grid.append([])
            for j in range(3):
                s_grid[i].append('')
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == val:
                position_val = [row, col]
    grid_x = 0
    grid_y = 0
    for row in range(position_val[0]-1, position_val[0]+2):
        for col in range(int(position_val[1])-1, int(position_val[1])+2):
            if row >= 0 and col >= 0:
                try:
                    s_grid[grid_x][grid_y] = grid[row][col]
                except:
                    grid_y += 1
                    continue
            grid_y += 1
        grid_x += 1
        grid_y = 0
    sub_g = [[],[],[]]
    row = 0
    col = 0
    for rows in range(3):
        for cols in range(3):
            if s_grid[rows][cols] != '':
                sub_g[rows].append(s_grid[rows][cols])
                row += 1
    for row in range(3):
        try:
            if sub_g[row] == []:
                del sub_g[row]
        except:
            continue
    final_grid = []
    for row in range(3):
        try:
            print(" ".join(map(str,sub_g[row])))
        except:
            continue


def main():
    print('Enter dimension:')
    dimension = int(input())
    print('Enter number in spiral:')
    number = int(input())
    sub_grid(create_spiral(dimension), number)
  # prompt user to enter dimension of grid

  # prompt user to enter value in grid

  # print subgrid surrounding the value

if __name__ == "__main__":
  main()