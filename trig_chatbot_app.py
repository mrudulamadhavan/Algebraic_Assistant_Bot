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
def preprocess_degrees(expr):
    replacements = {
        'sin 30': 'sin(pi/6)', 'cos 30': 'cos(pi/6)', 'tan 30': 'tan(pi/6)',
        'sin 45': 'sin(pi/4)', 'cos 45': 'cos(pi/4)', 'tan 45': 'tan(pi/4)',
        'sin 60': 'sin(pi/3)', 'cos 60': 'cos(pi/3)', 'tan 60': 'tan(pi/3)',
        'sin 90': 'sin(pi/2)', 'cos 90': 'cos(pi/2)', 'tan 90': 'tan(pi/2)'
    }
    for deg, rad in replacements.items():
        expr = expr.replace(deg, rad)
    return expr

def simplify_trig(expr):
    try:
        expr_preprocessed = preprocess_degrees(expr)
        parsed_expr = parse_expr(expr_preprocessed, evaluate=True)
        simplified = simplify(parsed_expr)
        return expr, parsed_expr, simplified
    except Exception as e:
        return expr, expr, f"Error simplifying expression: {e}"

def solve_trig_equation(expr):
    try:
        expr_preprocessed = preprocess_degrees(expr)
        parsed_expr = parse_expr(expr_preprocessed, evaluate=False)
        equation = Eq(parsed_expr, 0)
        solution = solveset(equation, x, domain=S.Reals)
        return equation, solution
    except Exception as e:
        return expr, f"Error solving equation: {e}"

def explain_trig(expr):
    try:
        raw, parsed_expr, simplified = simplify_trig(expr)
        steps = f"1. Original Expression: $${raw}$$\n"
        steps += f"2. Converted to Radians: $${parsed_expr}$$\n"
        steps += f"3. Simplified Result: $${simplified}$$"
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
        eqn, solution = solve_trig_equation(query)
        st.latex(f"1. Equation: {eqn}")
        st.latex(f"2. Solution Set: {solution}")
    elif intent == 'simplify_expression':
        raw_expr, parsed_expr, simplified = simplify_trig(query)
        st.latex(f"1. Original Expression: {raw_expr}")
        st.latex(f"2. Converted to Radians: {parsed_expr}")
        st.latex(f"3. Simplified Result: {simplified}")
    elif intent == 'inverse_trig':
        st.write("📘 This involves inverse trigonometric functions. Currently supports `asin`, `acos`, `atan`.")
        try:
            parsed = parse_expr(query)
            st.latex(f"1. Expression: {query}")
            st.latex(f"2. Evaluated Result: {parsed.evalf()}")
        except:
            st.write("Could not evaluate inverse function.")
    else:
        st.warning("❓ Unable to classify your query. Try a different format or use sin/cos/tan.")

   

st.sidebar.title("🧮 Advanced Features")
st.sidebar.info("We track your queries anonymously and assign rewards to improve our learning agent.")

