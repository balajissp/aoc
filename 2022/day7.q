fs:(`$"..") _ (!) . flip {(`$p:1_x 0;{$[x like "dir *";`$4_x;"J"$first " " vs x]}each 2 _ x)}each "\n"vs/: 1_"$ cd"vs i: "c"$read1`:day7.txt;
rec:{sum {$[-11h~type x;rec fs x;x]}each x};
sum sz where 100000 > sz:rec each fs 