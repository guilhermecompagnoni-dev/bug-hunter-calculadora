# Bug Hunter & TDD Calculator

## Descrição

Este projeto foi desenvolvido para a atividade **Bug Hunter & TDD Calculator**.

A proposta foi analisar uma calculadora científica em Python, identificar defeitos no código, registrar os bugs encontrados e aplicar a metodologia TDD para corrigir um dos problemas.

A calculadora possui operações como adição, subtração, multiplicação, divisão, potência, raiz quadrada, fatorial e logaritmos.

## Objetivo da atividade

O objetivo principal foi praticar:

- identificação de bugs;
- criação de relatórios de defeitos;
- uso de testes unitários;
- aplicação da metodologia TDD;
- versionamento e entrega pelo GitHub.

## Estrutura do projeto

```text
bug-hunter-calculadora/
│
├── Calculadora.py
├── test_calculadora.py
├── Bugs.md
└── README.md
## Funcionalidades

A calculadora oferece as seguintes operações:

- Adição
- Subtração
- Multiplicação
- Divisão
- Potenciação
- Raiz quadrada
- Fatorial
- Logaritmo natural
- Logaritmo base 10
- Seno
- Cosseno
- Tangente

---

## Fluxo do sistema

Fluxo simplificado da aplicação:

Início

↓

Usuário seleciona uma operação

↓

Sistema recebe os valores informados

↓

Sistema executa o cálculo

↓

Resultado exibido na tela

↓

Fim

---

## Especificação da interface

Entrada:
- Número da operação
- Valores numéricos necessários para o cálculo

Saída:
- Resultado da operação matemática
- Mensagens de erro quando necessário

---

## Armazenamento

A aplicação não utiliza banco de dados.

Todos os cálculos são realizados em memória durante a execução do programa.

---

## Integrações

O projeto utiliza a biblioteca NumPy para algumas operações matemáticas.

Não há integração com APIs externas ou serviços web.

---

## Execução

Para executar a calculadora:

```bash
python Calculadora.py
```

---

## Testes unitários

Para executar os testes:

```bash
python -m unittest
```

Os testes verificam o funcionamento correto da função fatorial.

---

## Quadro Trello

Link do quadro utilizado no projeto:

https://trello.com/invite/b/69e42cf2e220b2873dcd6ff9/ATTI1bfb243f56b9a5cfcc93e94f6637549f99D08BC0/agile-docs-code-sprint
