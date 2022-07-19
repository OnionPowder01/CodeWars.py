## Third Angle of a Triangle

**Definition**

You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.

### Solution

```python
def other_angle(a, b):
    return 180 - (a+b)
```
        
