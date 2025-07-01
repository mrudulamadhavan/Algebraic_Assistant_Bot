import streamlit as st
from sympy import symbols, Eq, simplify, expand, factor, solve, latex, sympify
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import json
import os
import random

x, y, z = symbols('x y z')
transformations = (standard_transformations + (implicit_multiplication_application,))

st.set_page_config(page_title="Algebra Assistant Bot", page_icon="📘")
st.title("📘 Algebraic Assistant Chatbot")

st.markdown("🔍 **Enter an algebraic expression or equation:**")
st.write("ℹ️ Use `**` for powers and `*` for multiplication.")
query = st.text_input("", placeholder="e.g., x**2 + 3*x = 10 or (x+2)*(x-3)")*(x-3)")

riddles_and_answers = [
    ("I’m always in the middle of algebra, but never in geometry. What am I?", "The letter 'b'"),
    ("I can be solved or simplified, expanded or factored. What am I?", "An equation"),
    ("The more you factor me, the simpler I become — until I disappear. Who am I?", "A polynomial"),
    ("You see me in every equation, yet I’m never alone. What am I?", "A variable"),
    ("I'm the silent partner in every operation, neither negative nor positive. Who am I?", "Zero")
]

thoughts = [
    "Mathematics is not about numbers, it's about understanding.",
    "Every equation holds a story — can you decode it?",
    "Simplicity is the ultimate sophistication in algebra.",
    "Equations teach us that every unknown has a reason.",
    "What you simplify today might be your breakthrough tomorrow."
]

def classify_algebra_intent(expr):
    if '=' in expr:
        return 'solve_equation'
    elif any(op in expr for op in ['*', '(', ')']):
        return 'expand_or_factor'
    else:
        return 'simplify'

def simplify_expression(expr):
    parsed_expr = parse_expr(expr, transformations=transformations)
    return simplify(parsed_expr)

def expand_expression(expr):
    parsed_expr = parse_expr(expr, transformations=transformations)
    return expand(parsed_expr)

def factor_expression(expr):
    parsed_expr = parse_expr(expr, transformations=transformations)
    return factor(parsed_expr)

def solve_equation(expr):
    left, right = expr.split('=')
    left_expr = parse_expr(left, transformations=transformations)
    right_expr = parse_expr(right, transformations=transformations)
    equation = Eq(left_expr, right_expr)
    return solve(equation)

def reward_for(intent):
    rewards = {
        'solve_equation': 1.0,
        'expand_or_factor': 0.8,
        'simplify': 0.6,
        'unknown': -0.5
    }
    return rewards.get(intent, 0.0)

def track_user_interaction(query, result_type):
    reward = reward_for(result_type)
    log_entry = {"query": query, "type": result_type, "reward": reward}
    with open("algebra_user_logs.json", "a") as log:
        log.write(json.dumps(log_entry) + "\n")
    return reward

def get_random_riddle():
    return random.choice(riddles_and_answers)[0]

def get_random_thought():
    return random.choice(thoughts)

if query:
    intent = classify_algebra_intent(query)
    reward = track_user_interaction(query, intent)
    st.subheader("🧠 Step-by-step Explanation")
    try:
        if intent == 'solve_equation':
            st.markdown("**Detected Task:** Solve the equation")
            solutions = solve_equation(query)
            st.markdown("**Original Equation:**")
            st.latex(query)
            st.markdown("**Solution:**")
            for i, sol in enumerate(solutions, 1):
                st.latex(f"x_{{{i}}} = {latex(sol)}")
        elif intent == 'expand_or_factor':
            st.markdown("**Detected Task:** Expand and Factor")
            expanded = expand_expression(query)
            factored = factor_expression(str(expanded))
            st.markdown("**Expanded Form:**")
            st.latex(latex(expanded))
            st.markdown("**Factored Form:**")
            st.latex(latex(factored))
        else:
            st.markdown("**Detected Task:** Simplify the expression")
            simplified = simplify_expression(query)
            st.markdown("**Simplified Result:**")
            st.latex(f"{query} = {latex(simplified)}")
    except Exception as e:
        st.error(f"❌ Error: {e}")

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        thumbs_up = st.button("👍 Yes")
    with col2:
        thumbs_down = st.button("👎 No")

    if thumbs_up:
        st.info("🧩 Curious Builder's Riddle: ")
        st.write(get_random_riddle())
    elif thumbs_down:
        st.info("🧠 Thought to Ponder: ")
        st.write(get_random_thought())


st.sidebar.title("📚 Supported Operations")
st.sidebar.markdown("""
- Simplify algebraic expressions
- Expand products of polynomials (including cubic expressions)
- Factor expressions (up to cubic polynomials)
- Solve linear, quadratic, and cubic equations
""")
st.sidebar.markdown("---")
st.sidebar.info("We track your queries anonymously and assign rewards to improve our algebra learning assistant.")

