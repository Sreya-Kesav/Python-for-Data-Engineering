# Day 3 - Strings

## 📚 Topics Covered

- Strings
- String Methods
- Method Chaining

---

## 📝 What is a String?

A string is simply text.

Anything inside single quotes (' ') or double quotes (" ") is a string.

Example:

```python
name = "Sreya"
city = "Chennai"
```

---

## 📝 String Methods

### upper()

Converts everything to uppercase.

```python
name.upper()
```

---

### lower()

Converts everything to lowercase.

```python
name.lower()
```

---

### title()

Capitalizes the first letter of every word.

```python
name.title()
```

---

### capitalize()

Capitalizes only the first letter of the sentence.

```python
name.capitalize()
```

---

### strip()

Removes extra spaces from the beginning and end.

```python
name.strip()
```

---

### replace()

Replaces one text with another.

```python
sentence.replace("SQL", "Python")
```

---

### len()

Returns the number of characters.

```python
len(name)
```

---

### split()

Splits a string into a list.

```python
name.split()
```

---

### find()

Returns the position of a word.

If not found, it returns -1.

```python
sentence.find("Python")
```

---

### startswith()

Checks if a string starts with something.

```python
filename.startswith("sales")
```

---

### endswith()

Checks if a string ends with something.

```python
filename.endswith(".csv")
```

---

## 📝 Method Chaining

Method chaining means calling multiple methods one after another.

Example:

```python
customer.strip().title().replace("Reddy", "Kesav")
```

Python executes the methods from left to right.

Method chaining makes the code shorter and cleaner.
