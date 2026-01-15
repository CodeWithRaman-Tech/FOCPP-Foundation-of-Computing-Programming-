**Week 3 – Summary Notes**
**Level 4, Semester 1, BSc (hons) Computing – Leeds Beckett University**
**“Control Statements – Fundamentals of Computer Programming”** 

# **Week 3 – Control Statements and Program Logic**

## **1. Purpose of This Week**

This week focuses on how programs make decisions and repeat actions.
It introduces **control statements**, which allow Python programs to implement logic and solve real problems.

The main topics are:

* Boolean expressions
* `if`, `elif`, and `else`
* Logical operators
* Loops (`while` and `for`)
* `break` and `continue`
* Ternary operator

---

## **2. Algorithms and Control Flow**

All computer programs are based on **algorithms**.
An algorithm is a set of logical steps used to solve a problem.

Every algorithm uses three main structures:

| Structure     | Meaning                     |
| ------------- | --------------------------- |
| **Sequence**  | Steps run one after another |
| **Selection** | Choosing which steps to run |
| **Iteration** | Repeating steps             |

Selection and iteration depend on **Boolean expressions** .

---

## **3. Boolean Expressions**

A **Boolean expression** gives a result of either:

* `True`
* `False`

They use **relational (comparison) operators** such as:

```
>   <   >=   <=   ==   !=
```

Example:

```python
age > 18
```

This returns `True` or `False` depending on the value of `age` .

---

## **4. The `if` Statement**

The `if` statement is used to make decisions.

Example:

```python
if number1 > number2:
    print("number1 is greater")
```

The indented code only runs if the condition is `True` .

---

## **5. `if…else` and `elif`**

`else` runs when the `if` condition is `False`.

Example:

```python
if number1 > number2:
    print("number1 is greater")
else:
    print("number2 is greater or equal")
```

`elif` is used to test more conditions:

```python
if number1 > number2:
    print("greater")
elif number1 == number2:
    print("equal")
else:
    print("smaller")
```

## **6. Logical Operators**

Logical operators combine multiple conditions.

| Operator | Meaning               |
| -------- | --------------------- |
| `and`    | True if both are True |
| `or`     | True if one is True   |
| `not`    | Reverses the result   |

Example:

```python
if age >= 18 and age <= 65:
    print("Working age")
```

Parentheses should be used for clarity:

```python
if (age >= 18 and age <= 65) or male:
```

## **7. Membership Testing**

Python can check if a value exists in a string or list.

Example:

```python
if "Eric" in names:
    print("Eric is in the list")
```

```python
if word not in sentence:
    print("Word not found")
```
## **8. Ternary Operator**

A **ternary operator** is a short form of `if…else` that returns a value.

Syntax:

```python
value1 if condition else value2
```

Example:

```python
highest = a if a > b else b
```

## **9. The `while` Loop**

A `while` loop repeats while a condition is `True`.

Example:

```python
x = 10
while x > 0:
    print(x)
    x = x - 1
```

## **10. The `for` Loop**

A `for` loop repeats for each item in a sequence.

Example:

```python
names = ["Terry", "John", "Eric"]
for n in names:
    print(n)
```

## **11. The `range()` Function**

`range()` generates numbers for loops.

Example:

```python
for i in range(10):
    print(i)   # 0 to 9
```

With step:

```python
for i in range(10, 20, 2):
    print(i)
```

## **12. `break` and `continue`**

* `break` stops a loop early
* `continue` skips to the next loop round

Example:

```python
for n in names:
    if n == "John":
        break
```

Example:

```python
for n in names:
    if "a" in n:
        continue
    print(n)
```

## **13. Nested Loops**

A loop inside another loop is called a **nested loop**.

Example:

```python
for i in range(1, 5):
    for j in range(1, 5):
        print(i, j)
```

Too much nesting can make programs slow and hard to read .

---

## **14. Week 3 Key Learning Summary**

In Week 3 we learned:

* Programs use **selection** and **iteration**
* Decisions are made using Boolean expressions
* `if`, `elif`, and `else` control program flow
* `while` and `for` create loops
* `break` and `continue` control loops
* Ternary operators return values based on conditions
* Code blocks can be nested
