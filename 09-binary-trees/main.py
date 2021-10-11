from trees import Tree

print("Árvores Binárias")
menu = -1
tree = Tree()

while menu != 0:
  print(" 1. Printar árvore")
  print(" 2. Inserir")
  print(" 3. Buscar")
  print(" 4. Printar Em Ordem (ERD)")
  print(" 5. Printar Pré Ordem (RED)")
  print(" 6. Printar Pós Ordem (EDR)")
  print(" 7. Altura da Árvore")
  print(" 0. Sair")

  menu = int(input("Digite a opção desejada: "))

  if menu == 1:
    print(tree)
  elif menu == 2:
    elemento = int(input("Digite o elemento: "))
    tree.insert(elemento)
  elif menu == 3:
    elemento = int(input("Digite o elemento: "))
    if tree.get(elemento):
      print("Encontrado")
  elif menu == 4:
    tree.print_erd(tree.root)
  elif menu == 5:
    tree.print_red(tree.root)
  elif menu == 6:
    tree.print_edr(tree.root)
  elif menu == 7:
    print(f"Altura = {tree.height(tree.root)}")