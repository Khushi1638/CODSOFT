# 🔐 Task 2: Secure Password Generator

## 📝 Task Overview
Create a secure and interactive password generator that allows users to customize their password according to specific preferences:

- Specify password length (minimum 8 characters).
- Choose to include uppercase, lowercase, digits, and/or special characters.
- Ensure the generated password meets strength criteria.
- Option to generate another password in the same session.

---

## ⚙️ Features

- Enforces a minimum password length of 8 characters.
- Interactive prompts for including character types.
- Input validation to ensure proper entries.
- Password strength classification (weak, moderate, strong).
- Modular design with reusable functions.

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
cd codsoft-internship-tasks/password-generator
```

### 4. Run the Password Generator
```bash
python password_generator.py
```

### 5. Use the Program
Follow the prompts to generate your custom password.

---

## 💡 What I Learned

- Working with Python modules like `random` and `string`.
- Validating user input and handling edge cases.
- Organizing code into clean, readable functions.
- Evaluating password strength based on complexity.

---

## 🧠 Password Strength Logic

| Criteria Met         | Password Length | Strength     |
|----------------------|------------------|---------------|
| All 4 character sets | >= 12 characters | Strong ✅      |
| 3+ character sets    | >= 10 characters | Moderate ⚠️    |
| Less than above      | < 10 characters  | Weak ❌        |

---

## 👀 Sample Interaction
```bash
✨ Welcome to the Secure Password Generator ✨

Enter the length for the password: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): n

🔑 Your generated password is:
R7ehxDLWv3Xp

✅ The password is strong.
Do you want to generate another password? (y/n): n
Thank you for using the password generator! 🔒
```

---

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

