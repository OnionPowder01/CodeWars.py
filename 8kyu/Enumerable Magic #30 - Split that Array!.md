## Enumerable Magic #30 - Split that Array!


**Definition**

Create a method partition that accepts a list and a method/block. It should return two arrays: the first, with all the elements for which the given block returned true, and the second for the remaining elements.

Here's a simple Ruby example:

```
Examples:
The equivalent in Python would be:

animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
partition(animals, lambda x: len(x) == 3)
    # (['cat', 'dog', 'cow'], ['duck', 'donkey'])
```

### Solution

```python
def partition(list1, classifier_method):
   tup = ()
   list2 = []
   final_list1 = list(filter(classifier_method , list1)) 
   for i in list1:
           if(i not in final_list1):
               list2.append(i)
   tup = (final_list1,list2)
   return tup
```
        
