from collections import Counter
import numpy as np
from pathlib import Path

data='''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4
1 3 6 7 9''' # sample

data=Path(__file__).with_suffix('.txt').read_text()
data=[np.array(list(map(int,row.split()))) for row in data.split('\n')]
# print(data)
def is_safe(lst:np.array):
    diffs = set(lst[1:]-lst[:-1])
    return diffs.issubset({1,2,3}) or diffs.issubset({-1,-2,-3})

ans1= sum(map(is_safe,data))
print(ans1)

def is_safe_damper(lst:np.array):
    diffs = Counter(lst[1:]-lst[:-1])
    return diffs.issubset({1,2,3}) or diffs.issubset({-1,-2,-3})

ans2 = sum(map(is_safe_damper,data))
print(ans2)
