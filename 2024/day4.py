from collections import Counter
import numpy as np
from pathlib import Path
import re
from itertools import zip_longest

data='''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX''' # sample

# data = '''..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....''' #sample2

data=Path(__file__).with_suffix('.txt').read_text()
def partial_sum(s):
    # print(s,'.'.join(s).count('XMAS'), '.'.join(s).count('SAMX'))
    return '.'.join(s).count('XMAS') + '.'.join(s).count('SAMX')

#q1
data=data.split('\n')
score=0
cols = [''.join(x) for x in zip(*data)]
l,c=len(data[0]),len(data)
print(l,c)
flat = ''.join(data)
right_diagonals = [flat[i:l*(c-i)+1:l+1] for i in range(c)] + [flat[i*l::l+1] for i in range(1,c)]
left_diagonals = [flat[i:(i+1)*l-1:l-1] for i in range(c)] + [flat[i*l-1::l-1] for i in range(c)]
# print(right_diagonals,left_diagonals)
for dirs in [data, cols, right_diagonals, left_diagonals]:
    ps=partial_sum(dirs)
    score+=ps
    print(ps,score)