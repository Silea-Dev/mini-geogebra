from mini_geogebra import core


if __name__ == "__main__":
    while True:
        choice = input("\nPlot a graph? [Y/N] (or 'exit' to quit): ")

        if choice.lower() == "exit":
            print("End.")
            break

        elif choice.lower() in ["y", "yes"]:
            formula_plot = core.data_graph()

            if formula_plot is not None:
                core.plot_graph(formula_plot)

        elif choice.lower() in ["n", "no"]:
            result_expression = core.data_expression()

            if result_expression is not None:
                print(f"Result: {result_expression}")

        else:
            print("[ERROR] Choise Y or N.")
