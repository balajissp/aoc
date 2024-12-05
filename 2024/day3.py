from collections import Counter
import numpy as np
from pathlib import Path
import re

data='''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))''' # sample

data=Path(__file__).with_suffix('.txt').read_text()
ptrn = re.compile(r"mul\((\d+),(\d+)\)|(do[\(\)]{2})|(don[\']t[\(\)]{2})")
result = 0
result2 = 0
flag=True
for m in re.findall(ptrn,data):
    print(m)
    #q1 
    if  m[0]!='' and m[1]!='':
        result += int(m[1]) * int(m[0])
    
    # q2 
    if m[2]: flag=True
    elif m[3]: flag=False
    elif flag is True:
        result2 += int(m[1]) * int(m[0])
    print(result,result2,flag)