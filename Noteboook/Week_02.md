**Week 1 – Summary Notes**
**Level 4, Semester 1, BSc (hons) Computing – Leeds Beckett University**
**“Variables and Types – Fundamentals of Computer Programming”** 


# **Week 1 – Variables, Data Types and Basic Python Concepts**

## **1. Purpose of This Week**

This week introduces the basic building blocks of Python programming.
It explains how data is stored, how values are processed, and how users interact with programs.

The main topics are:

* Variables and assignment
* Data types
* Functions
* Strings
* Lists
* User input

---

## **2. Variables**

A **variable** is used to store data in a program so it can be used later.

Example:

```python
age = 23
name = "Jon"
```

A variable has:

* A **name** (identifier)
* A **value**

Variable names:

* Must start with a letter or `_`
* Can contain letters, numbers, and `_`
* Are case-sensitive
  Example of good names:

```
age, student_name, highest_score
```

Invalid names:

1person, &value

## **3. Assignment**

The `=` symbol is used to assign a value to a variable.

Example:

```python
average = (10 + 20 + 30) / 3
```

The right side is calculated first, then the result is stored in the variable.

Variables can be updated:

```python
age = age + 1
```

Short forms (augmented assignment):

```python
count += 1
score *= 2
```


## **4. Data Types**

Every value in Python has a **data type**.

Common data types:

| Type    | Meaning         |
| ------- | --------------- |
| `int`   | Whole numbers   |
| `float` | Decimal numbers |
| `bool`  | True or False   |
| `str`   | Text (string)   |

Python is **dynamically typed**, meaning a variable’s type depends on the value stored.

Example:

```python
x = 10      # int
x = 10.5    # float
x = "hi"    # string
```

The `type()` function shows the data type.


---

## **5. Functions**

A **function** is a block of ready-made code that performs a task.

Example:

```python
print("Hello")
```

Functions:

* Are called using parentheses `()`
* Can take values (arguments)
* Can return results

Examples:

```python
type(10)
print("Total:", total)

## **6. Getting Input from the User**

The `input()` function is used to get data from the user.

Example:

```python
name = input("Enter your name: ")
```

Input is always read as a **string**.

To convert it:

```python
age = int(input("Enter age: "))


## **7. Strings**

A **string** is text stored in quotes.

Python supports:

* Single quotes `' '`
* Double quotes `" "`
* Triple quotes `""" """`

Example:

```python
"Hello"
'Welcome'
"""This is
a multi-line string"""
```

Escape characters:

* `\n` → new line
* `\t` → tab
* `\"` → double quote
* `\'` → single quote


## **8. String Indexing and Slicing**

Strings are sequences of characters.

Example:

```python
name = "Black Knight"
name[0]   # 'B'
name[-1]  # last letter
```

Slicing:

```python
name[0:5]   # 'Black'
name[:3]    # first 3 letters
name[6:]    # from index 6 to end


## **9. Lists**

A **list** stores multiple values in order.

Example:

```python
names = ["Terry", "John", "Eric"]
scores = [10, 20, 30]
```

Lists:

* Support indexing and slicing
* Can contain different data types
* Are **mutable** (can be changed)

Example:

```python
names[0] = "Mark"
```

## **10. Modifying Lists**

Add items:

```python
names.append("Sam")
```

Change or remove using slicing:

```python
scores[2:4] = [50, 60]
scores[-2:] = []
```

Length of list or string:

```python
len(names)
len("Hello")
```


## **11. Key Learning Summary**

In Week 1 we learned that:

* Variables store values
* Python uses dynamic data types
* Strings store text and use quotes
* Lists store multiple values and can be changed
* Functions like `print()` and `input()` are used for interaction
* Indexing and slicing allow access to parts of strings and lists
