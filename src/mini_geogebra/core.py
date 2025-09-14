import matplotlib.pyplot as plt
import numpy as np
import numexpr as ne
import re


def prepare_expression(expression_str):
    step_1 = expression_str.replace("^", "**")
    step_2 = re.sub(r"(\d)(x)", r"\1*\2", step_1)
    final_expression = step_2.replace(" ", "")
    return final_expression


def plot_graph(formula_str):
    x = np.linspace(-10, 10, 500)

    try:
        formatted_formula = prepare_expression(formula_str)
        y = ne.evaluate(formatted_formula)
        plt.plot(x, y)
        plt.title(f"Graph of Y = {formula_str}")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.show()
        return True
    except Exception:
        return False


def data_graph():
    formula_str = input("Enter a function using 'x' as the variable [exit]: ")
    if not formula_str:
        return None
    return formula_str


def data_expression():
    expression_str = input("Calculator: Enter an expression to evaluate: ")
    try:
        result = ne.evaluate(prepare_expression(expression_str))
        return result
    except Exception as e:
        return None
