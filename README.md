# S-Expression-To-Binary-Tree

### Problem
Given a binary tree of integers, determines whether there exists a root-to-leaf path whose nodes sum to a specified integer. Binary trees are represented in the input file as LISP S-expressions having the following form:

```
empty tree ()
tree empty tree OR (integer tree tree )
```
Note that with this formulation all leaves of a tree are of the form (integer () () )

### Input
The input consists of a sequence of test cases in the form of integer/tree pairs. Each test case consists of an
integer followed by one or more spaces followed by a binary tree formatted as an S-expression.
All binary tree S-expressions will be valid, but expressions may be spread over several lines and may contain
spaces. There are one or more test cases in an input file.

### Output
For each pair I,T (I represents the integer, T represents the tree) the output is the string yes if there is a
root-to-leaf path in T whose sum is I and no if there is no path in T whose sum is I.

### Sample
Sample Input:

```22 (5(4(11(7()())(2()()))()) (8(13()())(4()(1()()))))```


Sample Output:

```yes```
