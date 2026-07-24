# Day 2 - If, Else & Elif

## 📚 Topics Covered

- if
- else
- elif

---

## 📝 if

`if` is used when I want Python to execute a block of code only if a condition is True.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

If the condition is True, Python executes the code inside the `if` block.

---

## 📝 else

`else` is used when the `if` condition is False.

Example:

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Python skips the `if` block and executes the `else` block.

---

## 📝 elif

`elif` means **else if**.

I use it when there are multiple conditions to check.

Example:

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

Since `marks` is 82, the output will be:

```
Grade B
```

---

## 🧠 Things I Should Remember

- Python checks conditions from **top to bottom**.
- As soon as it finds the **first True condition**, it executes that block and stops checking the rest.
- That's why the **order of conditions is important**.
- Always write the **highest or most specific condition first**.


- Use `if` for the first condition.
- Use `elif` for additional conditions.
- Use `else` if none of the conditions are True.
