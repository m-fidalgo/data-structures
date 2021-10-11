from hashtables import HashTable

print("Tabelas de Espalhamento")
menu = -1
hashtable = HashTable()

while menu != 0:
  print(" 1. Printar tabela")
  print(" 2. Inserir")
  print(" 3. Remover")
  print(" 0. Sair")

  menu = int(input("Digite a opção desejada: "))

  if menu == 1:
    print(hashtable)
  elif menu == 2:
    elemento = int(input("Digite o elemento: "))
    if not hashtable.insert(elemento):
      print("Elemento já inserido")
  elif menu == 3:
    elemento = int(input("Digite o elemento: "))
    if not hashtable.remove(elemento):
      print("Elemento não contido na tabela")