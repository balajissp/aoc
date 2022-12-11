day 2:
```q
/ x y a 1
/ up z: x y a-z         [1 0 0;0 1 0;0 0 1; 0 -z -z]
/ down z: x y a+z       [1 0 0;0 1 0;0 0 1; 0 z z ]
/ forward z: x+z y-a*z a  [1 0 0;0 1 0;0 -z 1;z 0 0]
 
q) prd sum {(("up";"down";"forward")!(0 -1;0 1;1 0))[x]*y}. ("*J";" ") 0: `:p2.txt
q) (*). -1_ (0 0 0) {$[y[0]~"up";x - 0 0 1 * y[1]; y[0]~"down";x + 0 0 1 * y[1];x + (1,x[2],0)*y[1]] }/ flip ("*J";" ") 0: `:p2.txt
```


day 3: 
```q
l:read0 `:p3.txt

prd 2 sv/: 1 0=\:med each flip "1"=l
nb: til count first l;
m1:l {x where b={first where x=min x}01b#count each group b:x[;y]}/ nb;
m2:l {x where b={last  where x=max x}01b#count each group b:x[;y]}/ nb;
prd 2 sv/: m1,m2
```

day 5:
```q
ip:flip each ("JJ";",")0:/: flip ("* *";" ")0:`:p5.txt
rng:{x[0]+signum[d]*til each 1+abs d:x[1]-x[0]}

/part 1
vh:{x where any each (=)./: x} ip
sum 1<count each group p:raze (cross/)each rng each vh

/part 2
dg:{x where not any each (=)./: x} ip
sum 1<count each group p,0N!raze (,')./: rng each dg
```

day 6:
```q
i:0^@[;(1+til 8)] count each group first "J"$csv vs/: read0 `:p6.txt
f:{(0 0 0 0 0 1 0 0*x[0]) + 1 rotate x}
count 79 f/ i
count 255 f/ i
```

day 7:
```q
i: "J"$csv vs first read0`:p7.txt
min {sum abs x-y}[i] each {x[0]+til 1+x[1]-x[0]}(min;max)@\: i
"j"$min {sum {0.5*x*x+1}abs x-y}[i] each {x[0]+til 1+x[1]-x[0]}(min;max)@\: i
```

day 8:
```q
i:flip ("********** ****";" ") 0: `:p8.txt
(sum/) {(count each -4#x) in 2 3 4 7}each i
```

day 14:(not yet correct)
```q
i:flip ("SS*";" ") 0: `:p24.txt
map:(`inp`add`mul`div`mod`eql!(::;(+).;(*).;(div).;(mod).;{"j"$ (=). x}))
instr:{{[b;a]0N!a;a[1] set @[map[a 0];$[a[2]~"";b; get[a 1],value a 2]];0N! get each `w`x`y`z;z}[1;]each i}
monad: {[tst]`w`x`y`z set' 4#0; instr each 10 vs tst;get `z}

it:"j"$-1+10 xexp 14
while[not monad it;`it set it - 1]
it
```

day 25:
```q
i:read0`:p25.txt
f:{c# c _ ssr[;y,".";".",y] (3*c:count[x])#x}
fd:{flip f[;"v"]each flip x}
fl:f[;">"] each
iter: {fd fl x}
count iter scan i
```