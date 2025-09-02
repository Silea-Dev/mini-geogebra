import matplotlib.pyplot as plt
import numpy as np
import numexpr as ne
import re


def preparar_formula(formula_str):

    formula_passo_1 = formula_str.replace("^", "**")
    formula_passo_2 = re.sub(r"(\d)(x)", r"\1*\2", formula_passo_1)
    formula_final = formula_passo_2.replace(" ", "")
    return formula_final


while True:
    choice = input("Plot a grafic? [Y/N]: ")
    if choice.lower() == "sair" or not choice:
        print("Fim do programa!")
        break
    elif choice.lower() == "y" or choice.lower() == "yes":
        formula_str = input("Digite a Lei da Função que use 'x' como variável [exit]: ")
        if formula_str.lower() == "exit" or not formula_str:
            print("Fim do programa!")
            break
        else:
            print(f"Gerando gráfico para a função y = {formula_str}...")
            x = np.linspace(-10, 10, 100)
            try:
                y = ne.evaluate(preparar_formula(formula_str))
            except Exception as e:
                print("[ERROR] Algo saiu errado!")
                continue

            plt.plot(x, y)
            plt.title(f"Gráfico de Y = {formula_str}")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.grid(True)
            plt.show()

    elif choice.lower() == "n" or choice.lower() == "no":
        print("[ALERT] Digite as suas constantes!: ")
        conta_str = input("Calculadora: ")
        try:
            calculo = ne.evaluate(conta_str)
            print(f"Result: {calculo}")
        except Exception as e:
            print("[ERROR] Cuidado ao digitar suas constantes!")
            continue

    else:
        print("[ERROR] Faça uma choice!")
        continue
