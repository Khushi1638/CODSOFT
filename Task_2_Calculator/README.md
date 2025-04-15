# 📌 Task 1: Simple Calculator

## 📝 Task Overview
Build a simple calculator that performs basic arithmetic operations:

- Accept two numbers from the user.
- Prompt for an operation (+, -, *, /, %).
- Execute the chosen operation.
- Display the result clearly.


---

## ⚙️ Features

- Input validation for numeric values (integers and floats).
- Graceful handling of invalid operations.
- Proper error messages for division/modulo by zero.
- Clean control flow using Python’s `match-case` structure.
- Modular code organized into reusable functions.

---

## ▶️ How to Run the Program

### 1. Install Python
Download and install Python from the [official website](https://www.python.org/downloads/).

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/codsoft-internship-tasks.git
```
Or download the ZIP and extract it.

### 3. Navigate to the Project Folder
```bash
cd codsoft-internship-tasks/calculator
```

### 4. Run the Calculator
```bash
python calculator.py
```

### 5. Use the Program
Follow the on-screen prompts to perform calculations.

---

## 💡 What I Learned

- Handling user input and errors using `try-except`.
- Writing clean and readable code with modular functions.
- Using `match-case` for better readability and maintainability.
- Avoiding runtime errors with robust exception handling.

---

## 🧠 Program Flow

1. **Start with `main()`**: All execution begins in the `main()` function.
2. **Input Collection**:
   - Prompt the user to enter two numbers.
   - Re-prompts on invalid input (e.g., letters, empty input).
3. **Select Operation**:
   - Supported operations: +, -, *, /, %.
   - Handles invalid entries gracefully.
4. **Perform Calculation**:
   - Calls appropriate function based on user input.
   - Handles edge cases (e.g., division by zero).
5. **Display Output**:
   - Clearly prints the result or error message.

---

## 👀 Sample Interaction
```bash
Enter the first number: 15
Enter the second number: 0
Enter the operation (+, -, *, /, %): /
15.0 / 0.0 = Error: Division by zero is undefined.

Enter the first number: 8.5
Enter the second number: 2
Enter the operation (+, -, *, /, %): -
8.5 - 2.0 = 6.5
```



## 👩‍💻 Author
**Khushi Nagaliya**  
📍 Delhi, India  
🔗 [LinkedIn](https://www.linkedin.com/in/khushi-nagaliya) | ✉️ nagaliyakhushi@gmail.com

---

Each project is located in its own directory with a separate `README.md` explaining:
- The objective
- Features
- How to run the project
- Sample outputs
- Key learning outcomes
