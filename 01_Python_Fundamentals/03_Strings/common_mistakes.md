# ⚠️ Common Mistakes

## 1. replace() is case-sensitive

❌ Wrong

```python
sentence = "I love SQL"

print(sentence.replace("sql", "Python"))
```

Output:

```
I love SQL
```

Nothing changes because `"SQL"` and `"sql"` are different.

✅ Correct

```python
sentence.replace("SQL", "Python")
```

---

## 2. len() is a function, not a string method

❌ Wrong

```python
name.len()
```

✅ Correct

```python
len(name)
```