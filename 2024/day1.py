from collections import Counter
import numpy as np
from pathlib import Path

data='''3   4
4   3
2   5
1   3
3   9
3   3''' # sample

data=Path(__file__).with_suffix('.txt').read_text()

l1,l2=np.array([list(map(int,row.split())) for row in data.split('\n')]).T
ans1= sum(map(lambda x,y:abs(x-y), sorted(l1), sorted(l2)))
print(ans1)

scores = Counter(l1)
ans2 = sum(map(lambda x:x[0]*x[1]*scores[x[0]],Counter(l2).items()))
print(ans2)