# Dictionaries

## 📌 Overview

This project contains a set of Python functions that focus on **data transformation and grouping using dictionaries and lists**. Each function solves a specific problem such as inverting mappings or grouping data based on a shared property.

A corresponding **unittest suite** is provided to validate the correctness of each function.

---

## 🧠 What is Expected

You are required to implement the following functions inside a file called:

```
functions.py
```

Each function should:

* Take the given input data
* Transform or group it as specified
* Return a dictionary in the correct format

---

## 📂 Questions & Requirements

### ✅ Question 1: invert_employee_manager_map

**Input:**

```python
{"Alice": "M1", "Bob": "M1", "Clara": "M2"}
```

**Output:**

```python
{"M1": ["Alice", "Bob"], "M2": ["Clara"]}
```

**Task:** Group employees by their manager.

---

### ✅ Question 2: group_students_by_course

**Input:**

```python
[
    {"name": "Alice", "course": "Math"},
    {"name": "Bob", "course": "Math"},
    {"name": "Clara", "course": "Science"}
]
```

**Output:**

```python
{"Math": ["Alice", "Bob"], "Science": ["Clara"]}
```

**Task:** Group student names by course.

---

### ✅ Question 3: group_books_by_author

**Input:**

```python
[
    {"title": "Book1", "author": "A"},
    {"title": "Book2", "author": "A"},
    {"title": "Book3", "author": "B"}
]
```

**Output:**

```python
{"A": ["Book1", "Book2"], "B": ["Book3"]}
```

**Task:** Group book titles by author.

---

### ✅ Question 4: invert_country_city_map

**Input:**

```python
{"Paris": "France", "Lyon": "France", "Berlin": "Germany"}
```

**Output:**

```python
{"France": ["Paris", "Lyon"], "Germany": ["Berlin"]}
```

**Task:** Group cities by country.

---

### ✅ Question 5: group_numbers_by_parity

**Input:**

```python
[1, 2, 3, 4]
```

**Output:**

```python
{"odd": [1, 3], "even": [2, 4]}
```

**Task:** Separate numbers into odd and even.

---

### ✅ Question 6: group_employees_by_department

**Input:**

```python
[
    {"name": "Alice", "dept": "HR"},
    {"name": "Bob", "dept": "IT"},
    {"name": "Clara", "dept": "HR"}
]
```

**Output:**

```python
{"HR": ["Alice", "Clara"], "IT": ["Bob"]}
```

**Task:** Group employees by department.

---

### ✅ Question 7: invert_product_category_map

**Input:**

```python
{"Laptop": "Tech", "Phone": "Tech", "Shirt": "Clothing"}
```

**Output:**

```python
{"Tech": ["Laptop", "Phone"], "Clothing": ["Shirt"]}
```

**Task:** Group products by category.

---

### ✅ Question 8: group_words_by_first_letter

**Input:**

```python
["apple", "banana", "avocado"]
```

**Output:**

```python
{"a": ["apple", "avocado"], "b": ["banana"]}
```

**Task:** Group words based on their first letter.

---

### ✅ Question 9: invert_teacher_student_map

**Input:**

```python
{"Student1": "TeacherA", "Student2": "TeacherA", "Student3": "TeacherB"}
```

**Output:**

```python
{"TeacherA": ["Student1", "Student2"], "TeacherB": ["Student3"]}
```

**Task:** Group students by teacher.

---

### ✅ Question 10: group_transactions_by_type

**Input:**

```python
[
    {"amount": 100, "type": "deposit"},
    {"amount": 50, "type": "withdraw"},
    {"amount": 200, "type": "deposit"}
]
```

**Output:**

```python
{"deposit": [100, 200], "withdraw": [50]}
```

**Task:** Group transaction amounts by type.

---

---

### 2️⃣ Run all tests

In your terminal, navigate to the project folder and run:

```bash
python3 -m unittest test_functions.py
```

---

### 3️⃣ Run a single test (optional)

To run a specific test:

```bash
python3 -m unittest test_functions.TestFunctions.test_q1
```

---


---
