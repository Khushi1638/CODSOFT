# 💻 CODSOFT Internship Tasks

This repository will contain all the tasks completed during my internship at **CODSOFT**.  
Each task is implemented using **Python** and organized clearly for easy reference.  
It showcases my **learning progress**, **problem-solving skills**, and **hands-on experience** with Python throughout the internship.

> ⚠️ This is the **simplest version** of the calculator. This repository will also include two more projects:
> 1. Password Generator 🔐
> 2. Rock Paper Scissors Game ✊📄✂️

---

## 📌 Task: Simple Calculator

### 📝 Task Description
Design a simple calculator that performs basic arithmetic operations:

- Prompt the user to input two numbers.
- Ask for the operation to perform (`+`, `-`, `*`, `/`, `%`).
- Perform the selected operation.
- Display the result.

### ⚖️ Features
- User input validation for numbers.
- Handles invalid operation input.
- Gracefully handles division/modulus by zero.
- Uses Python’s `match-case` structure for clean operation control.
- Modular design using separate functions for each operation.

### ▶️ How to Run
To run this code on your local computer:

1. **Install Python**
   - Download Python from the [official Python website](https://www.python.org/downloads/) and install it.

2. **Clone or Download the Repository**
   - Clone this repo:
     ```bash
     git clone https://github.com/your-username/codsoft-internship-tasks.git
     ```
   - Or download the `.zip` file and extract it.

3. **Navigate to the Project Folder**
   ```bash
   cd codsoft-internship-tasks
   ```

4. **Run the Calculator Program**
   ```bash
   python calculator.py
   ```

5. **Follow the On-Screen Prompts**
   - Enter two numbers and choose an operation to see the result.

### 🧠 What I Learned
- Input validation using `try-except`.
- Handling division errors.
- Clean and readable code structure.
- Modular programming in Python.
- Using `match-case` for better code clarity.

---

## 💪 How the Code Works

1. **Program Starts with `main()`**  
   The program execution starts from the `main()` function.

2. **Step 1: Get Valid Numbers from the User**
   - It asks the user to enter two numbers (supports **integers** and **floats**).
   - If the user types anything that's not a number (like letters or symbols), it will show:  
     `"Please enter a valid number..."`  
     and ask again.

   ✅ Example:
   ```
   Enter the first number: 10
   Enter the second number: 5
   ```

3. **Step 2: Ask for an Operation**
   - The program then prompts the user to choose a math operation: `+`, `-`, `*`, `/`, or `%`.
   - If the user enters something invalid (like `^` or `&`), it will print an error message and ask again.

   ✅ Example:
   ```
   Enter the operation (+, -, *, /, %): *
   ```

4. **Step 3: Perform the Operation**
   - The chosen operation is matched using Python's `match-case` structure.
   - It calls the relevant function: `add()`, `subtract()`, `multiply()`, `divide()`, or `remainder()`.
   - Each function does the math and returns the result.

   ❗ Division and remainder operations are safely handled. If the second number is 0, the program will return:
   ```
   Error: Division by zero is undefined.
   ```

5. **Step 4: Display the Result**
   - Finally, the program prints the result of the calculation in a clear format.

   ✅ Example Output:
   ```
   10.0 * 5.0 = 50.0
   ```

---

### 👀 Sample Interaction

```bash
Enter the first number: 15
Enter the second number: 0
Enter the operation (+, -, *, /, %): /
15.0 / 0.0 = Error: Division by zero is undefined.
```

```bash
Enter the first number: 8.5
Enter the second number: 2
Enter the operation (+, -, *, /, %): -
8.5 - 2.0 = 6.5
```

---

> ✨ This calculator task is part of my journey toward becoming a better Python developer. Thanks to CODSOFT for the opportunity!


