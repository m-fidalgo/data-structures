from vectors import Vector

print("Vetores")
tamanho = int(input("Tamanho do vetor: "))

menu = -1
vetor = Vector(tamanho)

while menu != 0:
  print(" 1. Printar vetor")
  print(" 2. Inserir em certa posição")
  print(" 3. Inserir no final")
  print(" 4. Ver se o elemento existe")
  print(" 5. Índice do elemento")
  print(" 6. Remover pelo índice")
  print(" 7. Remover por elemento")
  print(" 0. Sair")

  menu = int(input("Digite a opção desejada: "))

  if menu == 1:
    print(vetor)
  elif menu == 2:
    pos = int(input("Digite a posição: "))
    elemento = int(input("Digite o elemento: "))
    vetor.insert_at(pos, elemento)
  elif menu == 3:
    elemento = int(input("Digite o elemento: "))
    vetor.insert_end(elemento)
  elif menu == 4:
    elemento = int(input("Digite o elemento: "))
    if vetor.contains(elemento):
      print("O elemento está no vetor")
    else:
      print("O elemento não está no vetor")
  elif menu == 5:
    elemento = int(input("Digite o elemento: "))
    print(f"Índice: {vetor.index(elemento)}")
  elif menu == 6:
    pos = int(input("Digite a posição: "))
    vetor.remove_at(pos)
  elif menu == 7:
    elemento = int(input("Digite o elemento: "))
    vetor.remove_element(elemento)


    

  


