# 📘 Algebra Assistant Bot

🧠 Objective:
An interactive Streamlit-based chatbot that helps users:

    🔹 Simplify expressions    
    🔹 Expand & factor polynomials (linear → cubic)    
    🔹 Solve algebraic equations    
    🔹 Learn through AI-powered reinforcement and riddles






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
