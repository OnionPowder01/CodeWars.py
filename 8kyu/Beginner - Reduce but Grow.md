## Beginner - Reduce but Grow


**Definition**

Given a non-empty array of integers, return the result of multiplying the values together in order. 

```Examples:
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
```

### Solution

```python
def grow(arr):
    total = 1
    for i in arr:
        total = total * i
    return total
```
        
