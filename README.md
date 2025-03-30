# Understanding the `if...elif...else` Statement in Python

The `if...elif...else` statement allows you to handle multiple conditions sequentially. Here’s how it works:

## Structure

- **`if`**: The first condition is checked.
  - If `True`, its code block runs, and the rest are skipped.
  - If `False`, Python moves to the next condition.
- **`elif`** (Short for "else if"):
  - If the previous conditions are `False`, this condition is checked.
  - You can have multiple `elif` blocks for complex logic.
- **`else`**:
  - Acts as the "default" case if all previous conditions fail.

---

## Example Breakdown

```python
temperature = 15

if temperature > 25:
    print("It's a hot day!")      # Block 1
elif temperature > 15:
    print("It's a warm day!")     # Block 2
else:
    print("It's a cold day!")     # Block 3
```

## Practice Questions

#### Q1: What will this code print?

```bash score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B") # This will print since 85 >= 80
elif score >= 70:
    print("C")
else:
    print("F")
```

#### Q2: Fixed age classification code

```bash
age = 15
if age < 13:
print("Child")
elif age < 20:
print("Teen") # This will print since 13 <= 15 < 20
else:
print("Adult")
```

#### Q3: Temperature classification

```bash
temp = 15
if temp <= 0:
    print("Freezing")
elif temp <= 10:
    print("Chilly")
elif temp <= 20:
    print("Moderate") # This will print since 10 < 15 <= 20
else:
print("Warm")
```

#### Q4: Bug demonstration

```bash
x = 5
if x > 3:
    print("A") # This prints since 5 > 3, other blocks skipped
elif x > 1:
    print("B")
else:
print("C")
```
