import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J4/input.txt'

with open(__path__, 'r') as file:
    #data = file.read().splitlines()
    matrice = [list(ligne.strip()) for ligne in file]

# Part 1
def letter_adjacent(matrice, i, j, lettre) :
    liste_co = []
    if i > 0 and matrice[i-1][j] == lettre :
        liste_co.append((i-1, j))
    if i < len(matrice) - 1 and matrice[i+1][j] == lettre :
        liste_co.append((i+1, j))
    if j > 0 and matrice[i][j-1] == lettre :
        liste_co.append((i, j-1))
    if j < len(matrice[0]) - 1 and matrice[i][j+1] == lettre :
        liste_co.append((i, j+1))
    if i > 0 and j > 0 and matrice[i-1][j-1] == lettre :
        liste_co.append((i-1, j-1))
    if i < len(matrice) - 1 and j < len(matrice[0]) - 1 and matrice[i+1][j+1] == lettre :
        liste_co.append((i+1, j+1))
    if i > 0 and j < len(matrice[0]) - 1 and matrice[i-1][j+1] == lettre :
        liste_co.append((i-1, j+1))
    if i < len(matrice) - 1 and j > 0 and matrice[i+1][j-1] == lettre :
        liste_co.append((i+1, j-1))
    return liste_co

def check_MAS_aligned(matrice, i_x, j_x, i_m, j_m) :
    # i_x, j_x is the position of X
    # i_m, j_m is the position of M
    i_dir = i_m - i_x
    j_dir = j_m - j_x
    if (i_m + 2*i_dir < 0 or i_m + 2*i_dir >= len(matrice[0])) or (j_m + 2*j_dir < 0 or j_m + 2*j_dir >= len(matrice[1])) :
        return 0
    # Check if AS in the same line
    i_a = i_m + i_dir
    j_a = j_m + j_dir
    i_s = i_m + 2*i_dir
    j_s = j_m + 2*j_dir
    if matrice[i_a][j_a] == 'A' and matrice[i_s][j_s] == 'S' :
        return 1
    return 0

def count_XMAS(matrice) :
    len_x = len(matrice[0])
    len_y = len(matrice)
    count = 0
    for i in range(len_y) :
        for j in range(len_x) :
            if matrice[i][j] == 'X' :
                list_M = letter_adjacent(matrice, i, j, 'M')
                for co in list_M :
                    count += check_MAS_aligned(matrice, i, j, co[0], co[1])
                    
    return count
                

total_1 = count_XMAS(matrice)
print("Total part 1: ", total_1)

# Part 2
def isXMAS(matrice, i, j) :
    if (i == 0 or i == len(matrice[0])-1 ) or (j == 0 or j == len(matrice[1])-1) :
        return 0
    # Check if 2 of diagonals are M 
    # and the 2 others are S
    d_hg = matrice[i-1][j-1]
    d_hd = matrice[i-1][j+1]
    d_bg = matrice[i+1][j-1]
    d_bd = matrice[i+1][j+1]
    letters = ["M", "S"]
    if not (d_hd in letters and d_hg in letters and d_bg in letters and d_bd in letters) :
        return 0
    if (d_hg == d_hd and d_bg == d_bd and d_hg != d_bg) :
        return 1
    if (d_hg == d_bg and d_hd == d_bd and d_hg != d_hd) :
        return 1
    return 0
    
for i in range(len(matrice[0])) :
    for j in range(len(matrice[1])) :
        if matrice[i][j] == 'A' :
            total_2 += isXMAS(matrice, i, j)


print("Total part 2: ", total_2)