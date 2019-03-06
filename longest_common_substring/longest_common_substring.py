def print_grid(str1, str2, grid):
    for letter in str2:
        print(letter, end ='\t')
    print("")
    i = 0
    for row in grid:
        for column in row:
            print(column, end ="\t")
        print(str1[i])
        i += 1


def find_grid_max(grid):
    maxval = 0
    maxrow = 0
    maxcol = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            curr = grid[i][j]
            if (curr > maxval):
                maxval = curr
                maxrow = i
                maxcol = j
    return (maxval, maxrow, maxcol)

def lcs(str1, str2):
    grid = []
    for row in range(len(str1)):
        grow = []
        for column in range(len(str2)):
            grow.append(0)
        grid.append(grow)
    nrows = len(str1)
    ncols = len(str2)
    for i in range(0, nrows):
        for j in range(0, ncols):
            if (str1[i] == str2[j]):
                if (i - 1 >= 0 and j - 1 >= 0):
                    grid[i][j] = 1 + grid[i - 1][j - 1]
                else:
                    grid[i][j] = 1
    val, row, col = find_grid_max(grid)
    print(str1[row - val + 1: row + 1])
    

def test():
    str1 = "hoeajuanpedrolfhdaklfdafasdf"
    str2 = "ahfeoihoasdfkjfiejuanpedroongv"
    res = lcs(str1, str2)

test()