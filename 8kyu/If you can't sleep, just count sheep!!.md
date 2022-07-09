## If you can't sleep, just count sheep!!

**Definition**

If you can't sleep, just count sheep!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

### Solution

```python
def count_sheep(n):
    sheep = ''
    for i in range(n):
        sheep += f"{i + 1} sheep..."
    return sheep
```
        
