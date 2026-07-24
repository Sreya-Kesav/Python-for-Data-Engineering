# ⚠️ Common Mistakes

## 1. Extra space while writing a variable

I accidentally left an extra space while writing a variable, which caused VS Code to show a red squiggly line.

❌ Wrong

```python
marks = 82

 if marks >= 50:
    print("Pass")
```

✅ Correct

```python
marks = 82

if marks >= 50:
    print("Pass")
```

Always check for unnecessary spaces before `if`, `elif` or `else`.

---

## 2. Forgetting the colon (:)

❌ Wrong

```python
if age >= 18
```

✅ Correct

```python
if age >= 18:
```

Every `if`, `elif`, and `else` statement must end with a colon (`:`).