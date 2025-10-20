import matplotlib.pyplot as plt
import numexpr as ne
import numpy as np
import re
import os


class Calculadora:

    def prepare_expression(self, expressao):
        step_1 = expressao.replace("^", "**")
        step_2 = re.sub(r"(\d)(x)", r"\1*\2", step_1)
        expressao_final = step_2.replace(" ", "")
        return expressao_final

    def plot_graph(self, expressao):
        x = np.linspace(-10, 10, 500)

        try:
            formatar_formula = self.prepare_expression(expressao)
            y = ne.evaluate(formatar_formula)
            plt.plot(x, y)
            plt.title(f"Graph of Y = {expressao}")
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")
            plt.grid(True)
            plt.xlim(-10, 10)
            plt.ylim(-10, 10)
            plt.show()
            return True
        except Exception:
            return False

    def data_graph(self, formula_str):
        if not formula_str:
            return None
        return formula_str

    def data_expression(self, expressao):
        try:
            result = ne.evaluate(self.prepare_expression(expressao))
            return result
        except Exception as e:
            return None


def iniciar():
    chama = Calculadora()
    while True:
        escolha = input("[MENU]:\nPlot a graph[Y] | Calculator[N]| | exit[ex]: ")

        if escolha.lower() == "ex":
            print("End.")
            # os.system("cls")
            break

        elif escolha.lower() in ["y", "yes"]:
            print("Enter a function using 'x' as the variable | menu[back]: ")
            while True:
                formula_str = input("\nGraph: ")

                if formula_str.lower() == "back":
                    print("BACK MENU\n")
                    break

                formula_plot = chama.data_graph(formula_str)

                if formula_plot is not None:
                    formula_final = chama.prepare_expression(formula_str)
                    chama.plot_graph(formula_final)

        elif escolha.lower() in ["n", "no"]:
            print("Calculator: Enter an expression to evaluate | menu[back]: ")
            while True:
                expressao_str = input("Expression: ")

                if expressao_str.lower() == "back":
                    print("BACK MENU\n")
                    break

                result_expression = chama.data_expression(expressao_str)

                if result_expression is not None:
                    print(f"Result: {result_expression}\n")

        else:
            print("[ERROR] Choise Y or N.")
