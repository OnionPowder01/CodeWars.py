## Sum Mixed Array

**Definition**

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

```Examples:
n= 5, m=5: 25
n=-5, m=5:  0
```

### Solution

```python
def sum_mix(arr):
    total = 0
    for i in arr:
        total += int(i)
    return total
```
        
