**Name:** Yuvika Shendge
**UFID:** 61747967

## How to Run

```
python src/hvlcs.py < data/test1.in
* do in command prompt the < doesnt work in powershell
```

Expected output:
```
6
xyz
```

No installs needed

---

## Example Input (data/test1.in)
```
3
x 2
y 3
z 1
xxyyzz
xyz
```

## Example Output (`data/test1.out`)
```
6
xyz
```
The common subsequence xyz has value 2 + 3 + 1 = 6.
---

## Question 1:

To time the program on different inputs, run:

```
time python src/hvlcs.py < data/test3.in
```

The table below shows runtimes on 10 inputs of increasing string length.
All strings are at least 25 characters long. Tests 1 and 2 are excluded from this since less than 25 

| File | \|A\| | \|B\| | Time (seconds) |
|------|-------|-------|------------|
| test3.in  | 27    | 27    | 0.0466     |
| test4.in  | 51    | 51    | 0.0445     |
| test5.in  | 53    | 53    | 0.0424     |
| test6.in  | 80    | 81    | 0.0437     |
| test7.in  | 100   | 100   | 0.0477     |
| test8.in  | 145   | 140   | 0.0458     |
| test9.in  | 200   | 200   | 0.0493     |
| test10.in | 400   | 400   | 0.0713     |
| test11.in | 500  | 500  | 0.0990 |
| test12.in | 600  | 600  |  0.1011 |

All of the runtimes are super similar across all inputs
A slight upward growth is seen startting at test10 as the O(n*m) cost begins to show
which matches expected quadratic growth.

## Question 2:

Let dp[i][j] = maximum value of common subsequence of:
- `A[0..i-1]`
- `B[0..j-1]`

Recurrence:
- If characters match:
```
dp[i][j] = dp[i-1][j-1] + v(A[i-1])
```

- Else:
```
dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

Base Cases:
```
dp[i][0] = 0
dp[0][j] = 0
```

Why this works:
- If characters match we include it and add its value
- If they don't match we skip one and take the better option
- Base cases are 0 because an empty string has nothing to match to

## Question 3:

Pseudocode:
```
for i from 1 to n:
    for j from 1 to m:
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + value(A[i])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

Runtime:
```
O(n * m)
```
We fill every cell in an n x m table, each cell takes O(1)

Space:

```
O(n * m)
```
- We store the entire n x m table
