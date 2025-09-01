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
    escolha = input("Deseja o gráfico? [S/N]: ")
    if escolha.lower() == "sair" or not escolha:
        print("Fim do programa!")
        break
    elif escolha.lower() == "s" or escolha.lower() == "sim":
        formula_str = input("Digite a Lei da Função que use 'x' como variável [sair]: ")
        if formula_str.lower() == "sair" or not formula_str:
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

    elif escolha.lower() == "n" or escolha.lower() == "nao":
        print("[ALERT]Digite as suas constantes!: ")
        conta_str = input("Calculadora: ")
        try:
            calculo = ne.evaluate(conta_str)
            print(f"Resultado: {calculo}")
        except Exception as e:
            print("[ERROR] Cuidado ao digitar suas constantes!")
            continue

    else:
        print("[ERROR] Faça uma escolha!")
        continue
