/load directions
steps: flip("CJ";" ")0: `:day9.txt
mv: "RULD"!(1 0;0 1;-1 0;0 -1);

/rope head follows directions
head:(enlist 0 0) {x, last[x]+/:(mv y 0)*/: 1+til y 1}/ steps

/tail follows head
/ f: {1_ enlist[0 0] {x,enlist $[not 1=max abs d:y - last x;last[x]+signum d;last[x]]}/ x}
f: {$[1<>max abs d:y - x;x+signum d;x]}\;

/part 1
tail: f head
count group tail

/part 2 
/ each knot tail becomes head of next knot
lastknot:9 f/ head
count group lastknot
