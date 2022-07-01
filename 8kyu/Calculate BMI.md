## Calculate BMI

**Definition**

Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

### Solution

```python
def bmi(weight, height):
    calcul = weight / height ** 2
    if calcul < 18.5:
        return "Underweight"
    elif calcul < 25:
        return "Normal"
    elif calcul < 30:
        return "Overweight"
    else:
        return "Obese"
```
        
