# 📘 Algebra Assistant Bot

### 🧠 Problem Statement
Learners often struggle with understanding and solving algebraic expressions and equations due to lack of personalized guidance, step-by-step breakdowns, and interactive feedback. The goal of this project is to build an intelligent agentic assistant that analyzes, solves, simplifies, and teaches algebra through user interaction, reinforcement feedback, and curiosity-driven learning (riddles).

### 🧠 Objective

To develop an interactive, agentic AI-powered Algebra Assistant that:

> * Solves, simplifies, expands, and factors algebraic expressions and equations.
> * Supports user learning through step-by-step breakdowns, reinforcement tracking, and curiosity prompts (riddles/thoughts).




-------------------------------------------------------------------------------------------------

| Feature                     | Description                                                                 |
| --------------------------- | --------------------------------------------------------------------------- |
| ✏️ Expression Input         | Enter algebraic expressions or equations                                    |
| 🧠 Auto Task Classification | Automatically detects intent: simplification, expansion, factoring, solving |
| 🧮 Algebra Engine (SymPy)   | Uses `sympy` to symbolically evaluate algebraic expressions                 |
| 🧩 Riddle Mode              | If the task is correct, display a math riddle with the answer               |
| 💡 Thought Mode             | If incorrect or low reward, gives a motivational/reflective thought         |
| 📈 Reward-based Logging     | Reinforcement mechanism to adaptively log and improve interaction           |
| 📁 User Log File            | Saves all user queries, intent, and reward to `algebra_user_logs.json`      |

## 📂 File Structure

algebra_bot

├── algebra_bot.py  

├── algebra_user_logs.json 

└── README.md              

## 🔧 Tech Stack

* **Frontend:** Streamlit
* **Backend Logic:** SymPy for symbolic algebra
* **User Feedback Loop:** Thumbs up/down for reinforcement
* **Data Logging:** JSON-based logging of user interactions

