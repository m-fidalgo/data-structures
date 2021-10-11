from maps import Map

print("Mapas")
menu = -1
map = Map()

while menu != 0:
  print(" 1. Printar mapa")
  print(" 2. Inserir")
  print(" 3. Remover")
  print(" 4. Obter elemento")
  print(" 0. Sair")

  menu = int(input("Digite a opção desejada: "))

  if menu == 1:
    print(map)
  elif menu == 2:
    chave = input("Digite a chave: ")
    elemento = input("Digite o elemento: ")
    map.insert(chave, elemento)
  elif menu == 3:
    chave = input("Digite a chave: ")
    if not map.remove(chave):
      print("Chave não encontrada")
  elif menu == 4:
    chave = input("Digite a chave: ")
    elemento = map.get_element(chave)
    if not elemento:
      print("Chave não encontrada")
    else:
      print(f"Elemento {elemento}")