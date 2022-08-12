## Beginner Series #1 School Paperwork

**Definition**

The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored)..

```
For example:

1.08 --> 30
```

### Solution

```python
import math

def cockroach_speed(s):
    return math.floor(s * 28)
```
        
