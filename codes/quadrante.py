while True:
  # Lê as coordenadas X e Y
  x, y = map(int, input().split())

  # Encerra o loop se qualquer coordenada for zero
  if x == 0 or y == 0:
    break

  # Determina o quadrante com base nos valores de X e Y
  if x > 0 and y > 0:
    print("primeiro")
  elif x < 0 and y > 0:
    print("segundo")
  elif x < 0 and y < 0:
    print("terceiro")
  elif x > 0 and y < 0:
    print("quarto")
