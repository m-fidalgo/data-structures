from sets import Set

print("Sets")
menu = -1
set = Set()

while menu != 0:
  print(" 1. Printar set")
  print(" 2. Inserir numa posição")
  print(" 3. Inserir no fim")
  print(" 4. Remover por índice")
  print(" 5. Remover por elemento")
  print(" 0. Sair")

  menu = int(input("Digite a opção desejada: "))

  if menu == 1:
    print(set)
  elif menu == 2:
    pos = int(input("Digite a posição: "))
    elemento = int(input("Digite o elemento: "))
    set.insert_at(pos, elemento)
  elif menu == 3:
    elemento = int(input("Digite o elemento: "))
    set.insert(elemento)
  elif menu == 4:
    pos = int(input("Digite a posição: "))
    set.remove_at(pos)
  elif menu == 5:
    elemento = int(input("Digite o elemento: "))
    set.remove_element(elemento)



    

  


