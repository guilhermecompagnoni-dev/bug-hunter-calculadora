# Relatório de Bugs - Calculadora Científica

## Bug 1 - Erro na função de adição

A função de adição retorna um valor incorreto porque o primeiro número é somado duas vezes.

Código original:

```python
def adicao(x, y):
    return x + np.add(x, y)
```

O resultado da soma não corresponde ao valor esperado.

---

## Bug 2 - Erro na função fatorial

A função fatorial retorna valores incorretos porque o laço começa em zero. Como qualquer número multiplicado por zero resulta em zero, o cálculo fica comprometido.

Código original:

```python
def fatorial(x):
    fat = 1
    for i in range(x+1):
        fat *= i
    return fat
```

---

## Bug 3 - Erro no logaritmo natural

A função utiliza `np.ln(x)`, porém essa função não existe na biblioteca NumPy.

Código original:

```python
return np.ln(x)
```

O correto seria utilizar `np.log(x)`.

---

## Bug 4 - Erro no logaritmo base 10

A função deveria calcular logaritmo na base 10, porém utiliza `np.log(x)`, que calcula logaritmo natural.

Isso faz com que o resultado apresentado não corresponda ao cálculo esperado.

---

## Bug 5 - Funções trigonométricas incompletas

O menu apresenta opções para seno, cosseno e tangente, porém essas funções não foram implementadas corretamente.

Como consequência, algumas opções do menu geram erro durante a execução do programa.

---

# Correção realizada com TDD

O bug escolhido para correção foi o da função `fatorial`.

Código original:

```python
for i in range(x+1):
```

Código corrigido:

```python
for i in range(1, x + 1):
```

Foram criados testes unitários para validar o comportamento da função após a correção.

Após a execução dos testes, todos foram aprovados com sucesso.

```text
Ran 3 tests in 0.000s

OK
```
