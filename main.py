import timeit

def calcular_bonus(salario, tempo_casa, faltas):
  if salario < 2000:
    return 0
  if tempo_casa < 1:
    return 0
  if faltas > 5:
    return 0
  return salario * 0.10

def calcular_bonus_refatorado(salario, tempo_casa, faltas):
  if salario < 2000 or tempo_casa < 1 or faltas > 5:
    return 0
  return salario * 0.10

print(calcular_bonus(2500, 2, 1))
print(calcular_bonus_refatorado(1500, 2, 1))

tempo_antes = timeit.timeit("calcular_bonus(2500, 2, 1)", globals=globals(), number=1_000_000)
tempo_depois = timeit.timeit("calcular_bonus_refatorado(1500, 2, 1)", globals=globals(), number=1_000_000)

print(f"Versão Antes: {tempo_antes:.4f} segundos")
print(f"Versão Refatorada: {tempo_depois:.4f} segundos")