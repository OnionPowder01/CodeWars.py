## Invert values

**Definition**

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

```Examples:
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```

### Solution

```python
def invert(lst):
    total = []
    for i in lst:
        total.append(-i)
    return total
```
        
