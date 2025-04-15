# ✊📄✂️ Task 3: Rock Paper Scissors Game

## 📝 Task Overview
Create a terminal-based **Rock, Paper, Scissors** game in Python that allows a user to play against the computer.

- Take user input (rock, paper, or scissors).
- Generate computer's random choice.
- Determine the winner based on standard rules.
- Display results and maintain scores.
- Option to play multiple rounds.

---

## ⚙️ Features

- Interactive CLI-based gameplay
- Randomized computer choices using `random` module
- Keeps track of wins, losses, and draws
- Clean and clear round-by-round results
- Input validation for valid choices
- Option to play again without restarting the program

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
cd codsoft-internship-tasks/rock-paper-scissors
```

### 4. Run the Game
```bash
python rock_paper_scissors.py
```

### 5. Use the Program
Follow the prompts to enter your choice and view the results.

---

## 💡 What I Learned

- Using `random.choice()` for game logic
- Handling user inputs and validating them
- Creating loops for continuous gameplay
- Using emojis and formatting to enhance terminal UX
- Writing modular, readable Python code

---

## 🧠 Game Rules Logic

| User | Computer | Result         |
|------|----------|----------------|
| Rock | Scissors | User Wins ✅  |
| Scissors | Paper | User Wins ✅  |
| Paper | Rock | User Wins ✅  |
| Same | Same | Draw ⚖️         |
| Otherwise | - | Computer Wins ❌ |

---

## 👀 Sample Interaction
```bash
🎮 Welcome to Rock, Paper, Scissors!

Choose rock, paper or scissor: paper

User Choice: Paper 📄
💻 Computer chose: Rock 📈

🎉 You win!

📊 Score => You: 1 , Computer: 0 , Draw: 0

🔁 Do you want to play another round? (yes/no): no

🏁 Game Over!

📓 Final Score:
You: 1
Computer: 0
Draws: 0
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

