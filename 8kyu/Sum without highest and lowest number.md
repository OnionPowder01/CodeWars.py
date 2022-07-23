## Sum without highest and lowest number

**Definition**

Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

```
Examples:
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
```

### Solution

```python
def sum_array(arr):
    return 0 if not arr else sum(sorted(arr)[1:-1])
```
        
