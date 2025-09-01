# 📈 Mini-GeoGebra: Calculadora e Plotter de Funções

![Screenshot do Mini-GeoGebra em ação](screenshot.png)

## 📄 Descrição

Este projeto é uma ferramenta multifuncional desenvolvida em Python que serve tanto como uma calculadora de linha de comando quanto como um plotter para funções matemáticas de uma variável (`x`). O objetivo é fornecer uma interface simples e amigável para realizar cálculos rápidos e visualizar o comportamento de diferentes funções em um gráfico 2D.

Este projeto foi desenvolvido como parte da minha jornada de estudos em Ciência de Dados, aplicando conceitos de lógica de programação, manipulação de strings com Regex e o uso de bibliotecas fundamentais do ecossistema Python.

## ✨ Funcionalidades Principais

- **Modo Duplo:** Escolha entre usar a ferramenta como uma calculadora para expressões diretas ou como um plotter de gráficos.
- **Plotter de Funções:** Insira qualquer função de `x` e visualize seu gráfico instantaneamente.
- **Sintaxe Amigável:** A calculadora é inteligente! Ela aceita:
  - `x^2` para potência (convertido para `x**2`).
  - `5x` para multiplicação implícita (convertido para `5*x`).
- **Avaliação Segura:** Utiliza a biblioteca `numexpr` para calcular as expressões, evitando os riscos de segurança da função `eval()`.

## 🛠️ Tecnologias Utilizadas

- **Python**
- **NumPy:** Para a geração de arrays e cálculos numéricos.
- **Matplotlib:** Para a visualização e plotagem dos gráficos.
- **NumExpr:** Para a avaliação segura das expressões matemáticas.
- **Regex (módulo `re`):** Para o pré-processamento e correção das fórmulas inseridas pelo usuário.

## 🚀 Como Executar o Projeto

Para rodar este projeto na sua máquina, siga os passos abaixo:

1. **Clone o repositório:**

   ```bash
   git clone [https://github.com/Silea-Dev/nome-do-seu-repositorio.git](https://github.com/Silea-Dev/nome-do-seu-repositorio.git)
   cd nome-do-seu-repositorio
   ```
2. **Crie um ambiente virtual (Recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. **Instale as dependências:**
   **(INSTRUÇÃO: Crie um arquivo chamado `requirements.txt` e coloque dentro dele os nomes das bibliotecas. Para fazer isso, ative seu ambiente virtual e rode o comando: `pip freeze > requirements.txt`)**

   ```bash
   pip install -r requirements.txt
   ```
4. **Execute o programa:**

   ```bash
   python main.py
   ```

## 📈 Próximos Passos (Roadmap)

- [ ] **v2.0:** Implementar a plotagem de múltiplas funções no mesmo gráfico.
- [ ] Adicionar mais opções de customização para os gráficos (cores, estilos de linha).
- [ ] Permitir que o usuário defina o intervalo de `x` a ser plotado.

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

**(INSTRUÇÃO: O GitHub tem uma função para adicionar uma licença. Ao criar um arquivo, digite `LICENSE` como nome e ele te dará a opção de escolher um modelo. A licença "MIT" é a mais comum e simples para projetos de portfólio.)**
