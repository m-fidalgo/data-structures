from stacks import Stack

print("Pilhas")
menu = -1
pilha = Stack()

while menu != 0:
  print(" 1. Printar pilha")
  print(" 2. Inserir")
  print(" 3. Remover")
  print(" 0. Sair")

  menu = int(input("Digite a opção desejada: "))

  if menu == 1:
    print(pilha)
  elif menu == 2:
    elemento = int(input("Digite o elemento: "))
    pilha.push(elemento)
  elif menu == 3:
    pilha.pop()



    

  


