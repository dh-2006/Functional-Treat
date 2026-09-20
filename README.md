# 📊 Functional Treat

A simple **Python console-based Data Analyzer and Transformer** for entering, analyzing, filtering, and sorting numerical data.

This project is created to demonstrate important **Python functions, lists, recursion, lambda functions, and basic data handling** in a simple and practical way.

---

## 📌 Project Overview

The **Functional Treatr** is a menu-driven Python program that allows users to work with 1D and 2D data.

The project demonstrates:

- 1D and 2D Lists
- Built-in Functions
- User Defined Functions
- `*args`
- `**kwargs`
- `__doc__`
- Recursion
- Lambda Function
- `filter()`
- Global Variables
- Multiple Return Values
- `sort()` and `sorted()`
- Loops and Conditional Statements

The program provides a simple console interface where users can select different operations from the main menu.

---

## ✨ Main Features

| Option | Operation |
|---|---|
| 📥 1 | Input Data |
| 📋 2 | Display Data Summary |
| 🔢 3 | Calculate Factorial |
| 🔎 4 | Filter Data by Threshold |
| 🔃 5 | Sort Data |
| 📊 6 | Display Dataset Statistics |
| 🚪 7 | Exit |

---

## 🧠 Python Concepts Demonstrated

### 📋 Lists

Lists are used to store the entered data.

```python
data = []
```

The program supports both 1D and 2D lists.

### 🛠️ User Defined Functions

Different functions are created for different operations such as input, filtering, sorting, and calculating statistics.

### 🔢 Built-in Functions

The project uses basic built-in functions such as:

```python
len()
min()
max()
sum()
```

These functions are used to calculate basic information about the dataset.

### 🔁 Recursion

Recursion is used to calculate the factorial of a number.

```python
def calculate_factorial(number):
```

### 🏷️ Lambda Function

A lambda function is used with `filter()` to select values according to the entered threshold.

```python
filter(lambda x: x >= threshold, values)
```

### 📦 `*args`

`*args` is used to display multiple values through a user-defined function.

```python
def display_values(*args):
```

### 🔑 `**kwargs`

`**kwargs` is used to display dataset information in key-value form.

```python
def display_dataset_summary(**kwargs):
```

### 🌐 Global Variable

A global variable is used to store and update dataset information.

```python
data = []
dataset_summary = {}
```

### ↩️ Multiple Return Values

The statistics function returns multiple values together.

```python
return minimum, maximum, total_sum, average
```

### 🔃 Sorting

The program demonstrates both:

```python
data.sort()
```
for sorting the data.

---

## 🖥️ Program Preview

```text
Welcome to the Data Analyzer and Transformer Program

Main Menu:
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit

Please enter your choice:
```

---

## 🖼️ Output Preview

View the actual output of the program:

[![View Output](https://github.com/dh-2006/Functional-Treat/blob/main/output.png)](output.png)

---

## 🎥 Project Demo

Watch the complete working demonstration:

[![Watch Demo](https://img.shields.io/badge/▶️_Watch_Project_Demo-blue?style=for-the-badge)](YOUR_GOOGLE_DRIVE_DEMO_LINK)

---

## 💻 Source Code

View the complete Python source code:

[![Open Source Code](https://github.com/dh-2006/Functional-Treat/blob/main/Functional%20Treat.py)](Functional Tteat.py)

---

## ▶️ How to Run

### Requirements

- Python 3.x
- Any Python IDE or Terminal

### Run the Program

```bash
python data_analyzer.py
```

After running the program, the main menu will appear on the screen.

---

## 📂 Project Structure

```text
Data-Analyzer-and-Transformer/
│
├── Functional Treat.py
├── output.png
└── README.md
```

---

## 🎯 Learning Objectives

This project helps in understanding:

- How to work with 1D and 2D lists
- How built-in functions can be used for data analysis
- How to create and use user-defined functions
- How recursion works
- How lambda functions work with `filter()`
- How `*args` and `**kwargs` are used
- How multiple values can be returned from a function
- How sorting functions work
- How a menu-driven Python program is created

---

## 🔄 Program Flow

```text
        Start
          ↓
      Main Menu
          ↓
     Input Data
          ↓
    Select Operation
          ↓
 ┌────────┼─────────┐
 ↓        ↓         ↓
Summary  Filter    Sort
 ↓        ↓         ↓
Statistics / Factorial
          ↓
        Exit
```

---

## ✅ Basic Validation

The program includes simple validation for:

- Invalid main menu choice
- Invalid 1D/2D selection
- Performing operations before entering data
- Invalid sorting choice
- No values found after filtering

The validation is kept simple so that the program remains easy to understand.

---

## 🚀 Possible Future Improvements

The project can be extended with:

- 🔍 Searching specific values
- 📈 More statistical calculations
- 📊 Data visualization
- 💾 Saving data to a file
- 📂 Loading previously saved data
- 📑 Exporting results

---

## 👨‍💻 Project Information

**Project:** Finctional Treat 
**Language:** Python  
**Type:** Console-Based Application  
**Level:** Beginner  
**Purpose:** Python Data Analysis and Function Practice

---

⭐ **Thank you for checking out the project!**
