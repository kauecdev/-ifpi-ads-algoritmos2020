def main():
  
    menu = '*** Brincando com Listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar todos os valores da lista'
    menu += '\n 3 - Mostrar valor na posição especificada'
    menu += '\n 4 - Remover do final'
    menu += '\n 5 - Remover do início'
    menu += '\n 6 - Remover de posição específica'
    menu += '\n 7 - Inserir valor na posição específica'
    menu += '\n 8 - Mostrar quantos valores pares existem na lista'
    menu += '\n 9 - Mostrar quantos valores ímpares existem na lista'
    menu += '\n 10 - Mostrar quantos valores positivos existem na lista'
    menu += '\n 11 - Mostrar quantos valores negativos existem na lista'
    menu += '\n 12 - Mostrar quantos valores zerados existem na lista'
    menu += '\n 13 - Calcular média dos valores da lista'
    menu += '\n 14 - Contar quantidade de ocorrências de um valor'
    menu += '\n 15 - Dobrar todos os valores'
    menu += '\n 16 - Dobrar todos os valores múltiplos de um valor especificado'
    menu += '\n 17 - Limpar valores da lista'
    menu += '\n N - <Crie diversas opções com os dados> '
    menu += '\n 0 - Sair '
    menu += '\n\n Opção >>> '

    lista = []

    while True:  # Condição sempre verdadeira, só irá para em caso de break ou error
        opcao = int(input(menu))

        # Verificar operacao a fazer de acordo com a opcao
        if opcao == 1:
            # Listas quando passadas como argumentos e modificadas por
            # funções não é necessário retorná-las
            # Se modificar a lista dentro de um função, as variáveis que já
            # apontavam para ela, terão acesso a lista moficiada normalmente
            # Por isso nao está ```lista = inserir_valores(lista)````
            inserir_valores(lista)
        elif opcao == 2:
          mostrar_todos_valores(lista)
        elif opcao == 3:
          mostra_valor(lista)
        elif opcao == 4:
          remover_final(lista)
        elif opcao == 5:
          remover_inicio(lista)
        elif opcao == 6:
          remover_posicao_especifica(lista)
        elif opcao == 7:
          inserir_posicao_especifica(lista)
        elif opcao == 8:
          mostrar_qtd_pares(lista)
        elif opcao == 9:
          mostrar_qtd_impares(lista)
        elif opcao == 10:
          mostrar_qtd_positivos(lista)
        elif opcao == 11:
          mostrar_qtd_negativos(lista)
        elif opcao == 12:
          mostrar_qtd_zerados(lista)
        elif opcao == 13:
          media_valores(lista)
        elif opcao == 14:
          qtd_ocorrencia_valores(lista)
        elif opcao == 15:
          dobrar_valores(lista)
        elif opcao == 16:
          dobrar_valores_multiplos_de_n(lista)
        elif opcao == 17:
          lista.clear()
          input('<enter> to continue...')
        elif opcao == 0:  # sair do while
          break
        else:
          print('Opção Inválida')


def inserir_valores(lista):
    qtd = int(input('Quantos valores desejar inserir? '))

    for i in range(qtd):
        valor = int(input('Valor: '))
        lista.append(valor)

    print('Valores inseridos com sucesso!')
    input('<enter> to continue...')


def mostra_valor(lista):
    posicao = int(input('Qual posição? '))
    print('Valor buscado:')
    print(lista[posicao])

    input('<enter> to continue...')


def remover_final(lista):
  print(f'Valor da última posição ({lista[-1]}) foi removido da lista.')
  lista.pop()
  print(lista)
  
  input('<enter> to continue...')


def remover_inicio(lista):
  lista.pop(0)
  print("Valor da primeira posição removido da lista.")
  print(lista)

  input('<enter> to continue...')


def remover_posicao_especifica(lista):
  pos = int(input("Qual a posição do valor você deseja que seja removida? "))

  print(f"Valor da posição {pos} ({lista[pos]}) foi removido da lista.")
  lista.pop(pos)
  print(lista)

  input('<enter> to continue...')


def mostrar_todos_valores(lista):
  print(lista)

  input('<enter> to continue...')


def inserir_posicao_especifica(lista):
  pos = int(input("Em qual posição deseja inserir o novo valor? "))
  el = int(input("Qual valor deseja inserir? "))

  lista.insert(pos, el)
  print(lista)

  input('<enter> to continue...')

def mostrar_qtd_pares(lista):
  qtd_pares = 0

  for valor in lista:
    if valor % 2 == 0:
      qtd_pares += 1

  print(f"Quantidade de valores pares na lista: {qtd_pares}")

  input('<enter> to continue...')


def mostrar_qtd_impares(lista):
  qtd_impares = 0

  for valor in lista:
    if valor % 2 != 0:
      qtd_impares += 1

  print(f"Quantidade de valores ímpares na lista: {qtd_impares}")

  input('<enter> to continue...')


def mostrar_qtd_positivos(lista):
  qtd_positivos = 0

  for valor in lista:
    if valor >= 0:
      qtd_positivos += 1

  print(f"Quantidade de valores positivos na lista: {qtd_positivos}")

  input('<enter> to continue...')


def mostrar_qtd_negativos(lista):
  qtd_negativos = 0

  for valor in lista:
    if valor < 0:
      qtd_negativos += 1

  print(f"Quantidade de valores negativos na lista: {qtd_negativos}")

  input('<enter> to continue...')


def mostrar_qtd_zerados(lista):
  qtd_zerados = 0

  for valor in lista:
    if valor == 0:
      qtd_zerados += 1

  print(f"Quantidade de valores zerados na lista: {qtd_zerados}")

  input('<enter> to continue...')


def media_valores(lista):
  total = 0

  for valor in lista:
    total += valor
  
  media = total / len(lista)

  print(f"A média dos valores da lista é: {media}")

  input('<enter> to continue...')


def qtd_ocorrencia_valores(lista):
  total_ocorrencias = 0
  valor_especificado = int(input("Qual valor deseja que seja contado suas ocorrências na lista? "))

  if valor_especificado in lista:
    for valor in lista:
      if valor == valor_especificado:
        total_ocorrencias += 1
  else:
      print("O valor especificado não está na lista")
      input('<enter> to continue...')
      return

  print(f"Total de ocorrências do valor especificado ({valor_especificado}): {total_ocorrencias}")

  input('<enter> to continue...')


def dobrar_valores(lista):
  for pos_valor in range(len(lista)):
    lista[pos_valor] *= 2

  print("Os valores da lista foram dobrados com sucesso!")
  print(lista)

  input('<enter> to continue...')


def dobrar_valores_multiplos_de_n(lista):
  multiplo = int(input("Qual múltiplo? "))

  for pos_valor in range(len(lista)):
    if lista[pos_valor] % multiplo == 0:
      lista[pos_valor] *= 2

  print("Os valores da lista foram alterados com sucesso!")
  print(lista)

  input('<enter> to continue...')

main()