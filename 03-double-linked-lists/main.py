from double_lists import DoubleLinkedList

print("Listas Duplamente Ligadas")
menu = -1
lista = DoubleLinkedList()

while menu != 0:
  print(" 1. Printar lista")
  print(" 2. Inserir numa posição")
  print(" 3. Inserir no fim")
  print(" 4. Obter elemento do nó")
  print(" 5. Ver se o elemento existe")
  print(" 6. Índice do elemento")
  print(" 7. Remover por índice")
  print(" 8. Remover por elemento")
  print(" 0. Sair")

  menu = int(input("Digite a opção desejada: "))

  if menu == 1:
    print(lista)
  elif menu == 2:
    pos = int(input("Digite a posição: "))
    elemento = int(input("Digite o elemento: "))
    lista.insert_at(pos, elemento)
  elif menu == 3:
    elemento = int(input("Digite o elemento: "))
    lista.insert(elemento)
  elif menu == 4:
    pos = int(input("Digite a posição: "))
    elemento = lista.get_node_element(pos)
    if elemento == None:
      print("Não encontrado")
    else:
      print(f"Elemento {elemento}")
  elif menu == 5:
    elemento = int(input("Digite o elemento: "))
    if lista.contains(elemento):
      print("O elemento está na lista")
    else:
      print("O elemento não está na lista")
  elif menu == 6:
    elemento = int(input("Digite o elemento: "))
    print(f"Índice: {lista.index(elemento)}")
  elif menu == 7:
    pos = int(input("Digite a posição: "))
    lista.remove_at(pos)
  elif menu == 8:
    elemento = int(input("Digite o elemento: "))
    lista.remove_element(elemento)



    

  


