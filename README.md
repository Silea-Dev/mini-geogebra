# Mini-GeoGebra: Calculadora e Plotador de Funções

![Mini-GeoGebra em ação](screenshot.png)

## 🚀 Visão Geral

Este projeto é uma ferramenta desenvolvida em Python que atua tanto como uma calculadora de linha de comando quanto como um plotador gráfico para funções de variável única (`x`).

Mais do que apenas uma calculadora, **este projeto representa a interseção entre o Rigor Matemático e a Engenharia de Software**. Ele foi projetado para aplicar conceitos robustos de programação — como **Programação Orientada a Objetos (POO)** e **Clean Code** — para resolver um problema clássico de visualização matemática.

## ⚙️ Arquitetura & Refatoração

O aspecto mais crítico deste projeto é sua evolução arquitetural.

* **v1.0 (Procedural):** Inicialmente escrito como um script monolítico procedural. Embora funcional, era difícil de manter e escalar.
* **v2.0 (POO - Atual):** Toda a base de código foi refatorada utilizando **Programação Orientada a Objetos**.
    * **Desacoplamento:** A lógica matemática está separada da interface de usuário e entrada de dados.
    * **Extensibilidade:** Adicionar novas operações matemáticas ou trocar a biblioteca de plotagem gera atrito mínimo devido ao design modular das classes.
    * **Avaliação Segura:** Implementação de sanitização rigorosa de inputs para prevenir injeção de código.

## Principais Funcionalidades

- **Modo Duplo:** Alternância fluida entre calculadora de expressões diretas e plotador de gráficos de funções.
- **Parsing Inteligente:** Sintaxe amigável processada via Regex:
  - `x^2` é convertido automaticamente para `x**2` (padrão Python).
  - `5x` (multiplicação implícita) é convertido automaticamente para `5*x`.
- **Security First (Segurança):** Utiliza a biblioteca `numexpr` para avaliação em vez da perigosa função `eval()`, garantindo que inputs matemáticos não possam executar códigos arbitrários no sistema.

## 🛠️ Tech Stack

- **Core:** Python 3.x (Abordagem POO)
- **Matemática:** NumPy (Vetorização & Geração de Arrays)
- **Visualização:** Matplotlib
- **Segurança & Parsing:** NumExpr, RegEx (`re`)

## Como Rodar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Silea-Dev/mini-geogebra.git](https://github.com/Silea-Dev/mini-geogebra.git)
   cd mini-geogebra

## **Atualizações:**
   Irei reescrever em Java, para testar as diferentes possibilidades para a aplicação!
