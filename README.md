# 📘 Algebra Assistant Bot

## 🧠 Objective

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
