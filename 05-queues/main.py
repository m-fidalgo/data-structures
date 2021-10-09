from queues import Queue

print("Filas")
menu = -1
fila = Queue()

while menu != 0:
  print(" 1. Printar fila")
  print(" 2. Inserir")
  print(" 3. Remover")
  print(" 0. Sair")

  menu = int(input("Digite a opção desejada: "))

  if menu == 1:
    print(fila)
  elif menu == 2:
    elemento = int(input("Digite o elemento: "))
    fila.insert(elemento)
  elif menu == 3:
    fila.remove()



    

  


