# Question 1
def invert_employee_manager_map(mapping: dict) -> dict:

    new_mappings = {}
    for employee, manager in mapping.items():
        if manager not in new_mappings:
            new_mappings[manager] = []
        new_mappings[manager].append(employee)
    return new_mappings

# Question 2
def group_students_by_course(students: list) -> dict:

    subjects = {}

    for student in students:
        name = student["name"]
        course = student["course"]

        if course not in subjects:
            subjects[course] = []
        subjects[course].append(name)

    return subjects

# Question 3
def group_books_by_author(books: list) -> dict:

    Authors = {}

    for book in books:
        name = book["title"]
        course = book["author"]

        if course not in Authors:
            Authors[course] = []
        Authors[course].append(name)

    return Authors    

# Question 4
def invert_country_city_map(mapping: dict) -> dict:

    Countries = {}

    for key, value in mapping.items():
        if value not in Countries:
            Countries[value] = []
        Countries[value].append(key)
    return Countries

# Question 5
def group_numbers_by_parity(numbers: list) -> dict:

    numbers_dict = {}

    numbers_dict["odd"] = []
    numbers_dict["even"] = []

    for number in numbers:
        if number % 2 ==0 :
            numbers_dict["even"].append(number)
        else:
            numbers_dict["odd"].append(number)
    return numbers_dict

# Question 6
def group_employees_by_department(employees: list) -> dict:
 
    departments = {}

    for employee in employees:
        name = employee["name"]
        depart = employee["dept"]

        if depart not in departments:
            departments[depart] = []
        departments[depart].append(name)
    return departments

# Question 7
def invert_product_category_map(mapping: dict) -> dict:

    categories = {}

    for key, value in mapping.items():
        if value not in categories:
            categories[value] = []
        categories[value].append(key)
    return categories

# Question 8
def group_words_by_first_letter(words: list) -> dict:

    first_letter = {}

    for word in words:
        letter = word[0]
        if letter not in first_letter:
            first_letter[letter] = []
        first_letter[letter].append(word)
    return first_letter
    

# Question 9
def invert_teacher_student_map(mapping: dict) -> dict:

    Staff = {}

    for key, value in mapping.items():
        if value not in Staff:
            Staff[value] = []
        Staff[value].append(key)
    return Staff

# Question 10
def group_transactions_by_type(transactions: list) -> dict:
    """
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
    """
    new_transactions = {}

    for transaction in transactions:
        amount = transaction["amount"]
        type = transaction["type"]

        if type not in new_transactions:
            new_transactions[type] = []
        new_transactions[type].append(amount)
    return new_transactions