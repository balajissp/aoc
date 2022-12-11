First parsing the input:

q) s:{" "_last[x]!(flip reverse -1_x)except\: " "} "\n"vs first "\n\n" vs "c"$read1`:day5.txt

q) op:flip `cnt`frm`to!(" I C C";" ")0: "\n"vs last "\n\n" vs "c"$read1`:day5.txt

Alternatively, do both simultaneously:

q)`s`op set {(" "_last[x 0]!(flip reverse -1_x 0)except\: " ";flip `cnt`frm`to!(" I C C";" ")0:x 1)}  {(0,first where "" ~/: x) cut x}read0`:day5.txt

Part 1:

Perform the restacking:
q) {s[x`to]:s[x`to],(x`cnt)#reverse s[x`frm];s[x`frm]:neg[(x`cnt)]_s[x`frm]}each op

Read the top of stack:
q) last each value s


Part 2:
Perform the restacking:
q) {s[x`to]:s[x`to],neg[x`cnt]# s[x`frm];s[x`frm]:neg[(x`cnt)]_s[x`frm]}each op

Read the top of stack:
q) last each value s

