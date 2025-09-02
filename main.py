import matplotlib.pyplot as plt
import numpy as np
import numexpr as ne
import re


def prepare_expression(expression_string):
    step_1 = expression_string.replace("^", "**")
    step_2 = re.sub(r"(\d)(x)", r"\1*\2", step_1)
    final_expression = step_2.replace(" ", "")
    return final_expression


while True:
    choice = input("Plot a graph? [Y/N] (or 'exit' to quit): ")

    if choice.lower() == "exit":
        break

    if choice.lower() in ["y", "yes"]:
        formula_string = input("Enter a function using 'x' as the variable [exit]: ")

        if formula_string.lower() == "exit":
            break

        print(f"Generating graph for function y = {formula_string}...")
        x = np.linspace(-1, 1, 1000)

        try:
            formatted_formula = prepare_expression(formula_string)
            y = ne.evaluate(formatted_formula)

            plt.plot(x, y)
            plt.title(f"Graph of Y = {formula_string}")
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")
            plt.grid(True)
            plt.show()

        except Exception as e:
            print(f"[ERROR] Could not plot the graph. Details: {e}")
            continue

    elif choice.lower() in ["n", "no"]:
        expression_str = input("Calculator: Enter an expression to evaluate: ")
        try:
            result = ne.evaluate(prepare_expression(expression_str))
            print(f"Result: {result}")
        except Exception as e:
            print(f"[ERROR] Could not calculate. Details: {e}")
            continue

    else:
        print("[ERROR] Invalid choice. Please enter Y or N.")

print("Program finished.")
