# Advent Of Code day 1
[Problem page](https://adventofcode.com/2022/day/1)

Solutions:

## Naive implementation: we only need to add the numbers
```q
  i: 0 each "++"vs"+"sv read0`:day1.txt
  max i         /part 1
  sum -3#desc i /part 2
```

Performance:
```q
  q)\ts:1000 i: 0 each "++"vs"+"sv read0`:day1.txt
  2281 128144
```

## Greedy mode... 
Let's save resources!

Use sum instead of adding one by one
```q
  q)\ts:1000 i: {0 "sum ",x}each "  "vs" "sv read0`:day1.txt
  1765 130544
```

Perhaps use `value` instead of passing through the handle `0`
```q
  q)\ts:1000 i: {value "sum ",x}each "  "vs" "sv read0`:day1.txt
  1428 128464
```

`read0` splits the rows, and we join them back... But q doesn't care about newline chars, so why split at all?
```q
  q)\ts:1000 i:{value "sum ",x}each "\n\n" vs "c"$read1 `:day1.txt
  1212 40736
```
Wow! that was quite an improvement.

Knowing the datatype helps `sum` 
```q
  q)\ts:1000 {sum value x}each "\n\n" vs "c"$read1 `:day1.txt
  1009 40560
```

How about peach? (Guess I'm out of my mind at this point!)

With 8 slaves,
```q
  q)\ts:1000 {sum value x}peach "\n\n" vs "c"$read1 `:day1.txt
  717 40560
```
OK, seems like it was not too greedy. That's enough for this problem.

