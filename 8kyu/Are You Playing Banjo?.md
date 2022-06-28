## Are You Playing Banjo?

**Definition**

Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

```Examples:
name + " plays banjo" 
name + " does not play banjo"
```

### Solution

```python
def are_you_playing_banjo(name):
    name1 = name[0]
    name1 = name1.lower()
    if name1 == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
```
        
