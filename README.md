# Trabalho Prático: Consolidate Conditional Expression (Coding)

Este repositório foi desenvolvido como parte de um trabalho prático para a matéria de **Coding**, com o objetivo de demonstrar a aplicação da técnica de refatoração **Consolidate Conditional Expression** (Consolidar Expressão Condicional).

## 📌 O Problema
No código original, temos múltiplos blocos `if` separados que executam exatamente a mesma ação (retornar `0`). Essa estrutura gera duplicação desnecessária de código e dificulta a leitura e a compreensão rápida das regras de negócio.

## 🚀 A Solução
A técnica consiste em unificar essas condições em uma única linha utilizando o operador lógico `or`. Com isso, eliminamos a repetição, centralizamos a validação e deixamos o código muito mais limpo e legível.

## 📊 Medição de Performance (`timeit`)
Para analisar o comportamento prático do código, utilizamos o módulo nativo `timeit` do Python executando as funções 1 milhão de vezes:
* **Por que 1 milhão de iterações?** Como computadores modernos executam instruções simples em nanossegundos, uma única execução é rápida demais para o relógio do sistema capturar com precisão. O loop elevado acumula tempo suficiente para uma medição confiável.
* **O papel do `globals()`:** Funciona como um "GPS" para o `timeit`, permitindo que ele localize e execute corretamente as funções declaradas no escopo global do script através de uma string.

## 🎯 Conclusão e Objetivos Atingidos
* **Legibilidade e Manutenção:** O principal ganho da refatoração é a clareza. É muito mais simples dar manutenção e alterar regras em uma única expressão consolidada do que em vários blocos de validação espalhados.
* **Performance:** Na engenharia de software, priorizamos a legibilidade e a qualidade do código. O foco da técnica é facilitar a leitura humana e a manutenibilidade do sistema, superando pequenas variações de milissegundos no processamento.