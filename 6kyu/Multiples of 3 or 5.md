## Multiples of 3 or 5

**Definition**

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.


### Solution

```python
def solution(number):
    list = []
    for i in range(0,number):
        if i % 3 == 0 or i % 5 == 0:
            list.append(i)
    return sum(list)
```
