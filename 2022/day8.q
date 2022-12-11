i: read0`:day8.txt; /load input

/part 1
f:{x>prev maxs x}' ;
show (sum/)(or/)(f i;flip f flip i;(reverse') f (reverse') i;flip (reverse') f (reverse') flip i)


/part 2
inds: {x cross x}1+til count[i]-2  ;
d:{$[0b in x;1+?[x;0b];count x]}  / visible distance in single direction
show max {[y;z] prd d each i[y;z]>(reverse z#i y;(z+1) _ i y;reverse y#i[;z];(y+1) _ i[;z])}./: inds

