import streamlit as st
from sympy import symbols, sin, cos, tan, simplify, Eq, solveset, S, pi, degree, acos, asin, atan
from sympy.parsing.sympy_parser import parse_expr
from sympy.abc import x
import matplotlib.pyplot as plt
import numpy as np
import traceback
import json
import os

# --- Utility Functions ---
def simplify_trig(expr):
    try:
        parsed_expr = parse_expr(expr, evaluate=False)
        simplified = simplify(parsed_expr)
        return simplified
    except Exception as e:
        return f"Error simplifying expression: {e}"

def solve_trig_equation(expr):
    try:
        parsed_expr = parse_expr(expr, evaluate=False)
        equation = Eq(parsed_expr, 0)
        solution = solveset(equation, x, domain=S.Reals)
        return solution
    except Exception as e:
        return f"Error solving equation: {e}"

def explain_trig(expr):
    try:
        simplified = simplify_trig(expr)
        steps = f"1. Original Expression: $${expr}$$\n"
        steps += f"2. Simplified Expression: $${simplified}$$"
        return steps
    except:
        return "Could not generate explanation."

def classify_query_type(query):
    query = query.lower()
    if any(func in query for func in ['sin', 'cos', 'tan', 'sec', 'csc', 'cot']):
        if '=' in query:
            return 'solve_equation'
        else:
            return 'simplify_expression'
    elif any(func in query for func in ['asin', 'acos', 'atan']):
        return 'inverse_trig'
    else:
        return 'unknown'

def plot_unit_circle():
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), 1, color='blue', fill=False)
    ax.add_artist(circle)
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_aspect('equal')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_title('Unit Circle')
    st.pyplot(fig)

def plot_triangle():
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 0], 'k')  # base
    ax.plot([1, 1], [0, 1], 'k')  # height
    ax.plot([0, 1], [0, 1], 'k')  # hypotenuse
    ax.text(0.5, -0.1, 'adjacent', ha='center')
    ax.text(1.05, 0.5, 'opposite', va='center')
    ax.text(0.5, 0.5, 'hypotenuse', rotation=45)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Right Triangle: sin = opposite/hypotenuse')
    st.pyplot(fig)

def plot_trig_graph():
    x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    fig, ax = plt.subplots()
    ax.plot(x_vals, np.sin(x_vals), label='sin(x)')
    ax.plot(x_vals, np.cos(x_vals), label='cos(x)')
    ax.plot(x_vals, np.tan(x_vals), label='tan(x)', linestyle='dashed', alpha=0.6)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_ylim(-5, 5)
    ax.legend()
    ax.set_title('Trigonometric Functions')
    st.pyplot(fig)

def track_user_interaction(query, result_type):
    log_entry = {"query": query, "type": result_type, "reward": reward_for(result_type)}
    with open("user_logs.json", "a") as log:
        log.write(json.dumps(log_entry) + "\n")

def reward_for(intent):
    rewards = {
        'solve_equation': 1.0,
        'simplify_expression': 0.8,
        'inverse_trig': 0.6,
        'unknown': -0.5
    }
    return rewards.get(intent, 0.0)

# --- Streamlit UI ---
st.set_page_config(page_title="Trigonometry Assistant Bot", page_icon="📐")
st.title("📐 Trigonometry Assistant Chatbot")

query = st.text_input("🔍 Enter a trigonometry expression or equation (e.g., sin(x)**2 + cos(x)**2):")

if query:
    intent = classify_query_type(query)
    track_user_interaction(query, intent)

    st.subheader("🧠 Step-by-step Explanation")
    if intent == 'solve_equation':
        explanation = solve_trig_equation(query)
        st.latex(f"{query} = 0")
        st.write("**Solution Set:**", explanation)
    elif intent == 'simplify_expression':
        st.markdown(explain_trig(query))
    elif intent == 'inverse_trig':
        st.write("📘 This involves inverse trigonometric functions. Currently supports `asin`, `acos`, `atan`.")
        try:
            parsed = parse_expr(query)
            st.latex(f"{query} = {parsed.evalf()}")
        except:
            st.write("Could not evaluate inverse function.")
    else:
        st.warning("❓ Unable to classify your query. Try a different format or use sin/cos/tan.")

    st.subheader("📊 Visual Aid")
    if st.checkbox("Show Unit Circle"):
        plot_unit_circle()
    if st.checkbox("Show Right Triangle Diagram"):
        plot_triangle()
    if st.checkbox("Show Graphs of sin(x), cos(x), tan(x)"):
        plot_trig_graph()

st.sidebar.title("🧮 Advanced Features")
st.sidebar.info("We track your queries anonymously and assign rewards to improve our learning agent.")
