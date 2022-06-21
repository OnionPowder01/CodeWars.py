## Beginner Series #2 Clock

**Definition**
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

```Examples:
h = 0
m = 1
s = 1

result = 61000
```

### Solution

```python
def past(h, m, s):
    return (h * 3600000) + (m * 60000 ) + (s * 1000 )
```
        
