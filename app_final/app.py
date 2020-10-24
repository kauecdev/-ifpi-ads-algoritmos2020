# Incialmente importamos os módulos necessários para a execução da aplicação

import os
import json

def main():

  '''
    Nesta função main, armazenaremos o array de celulares e
    externalizamos a parte responsável por lidar com o gerenciamento
    de ações de acordo com a opção digitada, pois assim, ao termos uma
    incosistência no exception handler no menu_principal, a função possa
    ser reiniciada sem zerar o array de celulares.
  '''

  celulares = inicializar('celulares.bd')

  menu = tela_principal()

  opcao_escolhida = int(input(menu))

  menu_principal(opcao_escolhida, celulares, menu)


def menu_principal(opcao, celulares, menu):
  
  '''
    Esse exception handler vai nos garantir que o usuário
    só consiga inserir um valor númerico, onde n > 0 e esteja
    relacionado com uma das opções sugeridas no menu. Caso digite o
    valor digitado seja um número negativo ou um caractere não numérico,
    a função menu_principal será reiniciada.
  '''

  try:
    if opcao < 0:
        print("O valor não pode ser negativo\n")
        menu_principal(opcao, celulares, menu)

    while opcao != 0:
      if opcao == 1:
        criar_celular(celulares) 
      elif opcao == 2:
        listar_celulares(celulares)
      elif opcao == 3:
        listar_celular_por_modelo(celulares)
      elif opcao == 4:
        listar_celular_por_marca(celulares)

      input("<enter> to continue...\n")
      opcao = int(input(menu))
    
    finalizar('celulares.bd', celulares)
  except:
    print("Você digitou um caractere inválido.\n")
    menu_principal(opcao, celulares, menu)


def tela_principal():

  '''
    Menu de opções disponíveis inicialmente para o
    usuário acessar.
  '''

  menu = "*** App Cell ***\n"
  menu += "1 - Novo celular\n"
  menu += "2 - Listar celulares\n"
  menu += "3 - Listar celular por nome do modelo\n"
  menu += "4 - Listar celular por nome da marca\n"
  menu += "0 - Sair\n"
  menu += "\nopcao: "

  return menu


def inicializar(arquivo_banco): 

  '''
  Nessa função, inicializamos o nosso arquivo para persistência
  de dados. Primeiramente, fazemos uma verificação para saber se
  esse arquivo já existe no diretório. Caso não exista, o arquivo
  será criado automaticamente.
  '''

  celulares_carregados = []

  if os.path.exists(arquivo_banco):
    arquivo = open(arquivo_banco, 'r')
    dados = arquivo.readline()
    arquivo.close()
    celulares_carregados = json.loads(dados)

  return celulares_carregados


def finalizar(arquivo_banco, celulares):

  '''
    Por fim, convertemos a lista de celulares adicionados 
    durante a execução do programa para ser adicionada no
    arquivo de persistência.
  '''

  dados = json.dumps(celulares)

  arquivo = open(arquivo_banco, 'w')
  arquivo.write(dados)
  arquivo.close()


def listar_celulares(celulares):
  
  '''
    Função para retornar todos os celulares
    que foram cadastrados no banco.
  '''

  qtd_celulares = len(celulares)

  print("*** Lista de celulares cadastrados ***")
  if qtd_celulares == 0:
    print("Nenhum celular cadastrado. Acesse a opção 1 para realizar o cadastro.")
  else:
    for celular in celulares:
      print('\nModelo:', celular['nome'])
      print('Marca:', celular['marca'])
      print('Tamanho da Tela (em \"):', celular['tela'])
      print('Preço: R$', celular['preco'])
      print('Tem câmera frontal?', celular['cam_frontal'])
      print(12*'---')


def criar_celular(celulares):
  '''
    Função para criar um objeto 'celular'
    e retorná-lo.
  '''

  print("A seguir, insira os dados do novo celular: \n")

  nome = input("Nome: ")
  marca = input("Marca: ")
  tela = input("Tela(\"): ")
  preco = definir_preco()
  cam_frontal = temCameraFrontal()

  celular = {
    'nome': nome,
    'marca': marca,
    'tela': tela,
    'preco': preco,
    'cam_frontal': cam_frontal
  }

  celulares.append(celular)
  print("\nO celular foi cadastrado com sucesso!")


def temCameraFrontal():
  '''
    Função para verificar se o valor digitado pelo usuário
    é uma string de valor 's' ou 'n'. Caso não seja, ele chama a função novamente
    até que o usuário insira um valor correto e então o retorna.
  '''

  cam_frontal = input("Câmera frontal? (s/n): ")

  response = cam_frontal.lower()

  if response == 's' or response == 'n':
    return 'Sim' if response == 's' else 'Não'
  else:
    print("A resposta deve ser 's' para sim ou 'n' para não.")
    temCameraFrontal()


def definir_preco():
  '''
    Função para verificar se o valor digitado pelo usuário
    de fato é um número. Caso não seja, ele chama a função novamente
    até que o usuário insira um valor numérico e então o retorna.
  '''

  try:
    preco = float(input("Preço (R$): "))
    return preco
  except:
    print("O preço deve ser inserido em formato numérico.")
    definir_preco()


def novo_menu(celulares, celulares_por_parametro):
  
  '''
    Essa função só será executada caso seja selecionada as
    opções 3 e 4 do menu principal e sejam encontrados registros
    de celulares por modelo ou marca. Essa função exibirá um submenu
    para que possam ser executadas outras funcionalidades dentro da lista
    retornada pelos métodos de listar por marca ou listar por modelo.
  '''
  submenu = "\n*** Submenu ***\n"
  submenu += "1 - Mostrar detalhes do celular\n"
  submenu += "2 - Remover celular\n"
  submenu += "3 - Editar celular\n"
  submenu += "4 - Duplicar registro\n"
  submenu += "0 - Voltar ao início\n"
  submenu += "\nopcao: "

  opcao_submenu = int(input(submenu))

  while opcao_submenu != 0:
    if opcao_submenu == 1:
      mostrar_detalhes(celulares_por_parametro)
    elif opcao_submenu == 2:
      remover_celular(celulares, celulares_por_parametro)
    elif opcao_submenu == 3:
      editar_celular(celulares, celulares_por_parametro)
    elif opcao_submenu == 4:
      duplicar_registro(celulares, celulares_por_parametro)
  
    input("<enter> to continue...\n")
    opcao_submenu = int(input(submenu))


def listar_celular_por_modelo(celulares):

  '''
    Essa função irá primeiro verificar no banco se o nome digitado por ele
    bate completamente ou parcialmente com o nome dos modelos registrados no
    banco. Caso sim, a função irá exibir a um ou mais celulares que baterem com
    a pesquisa e executará a função de um submenu, para que opções mais detalhadas
    sejam disponibilizadas para o usuário executar.
  '''

  nome_modelo = input("Digite o nome do modelo: ")

  celulares_por_modelo = []

  for celular in celulares:
    if nome_modelo in celular['nome']:
      celulares_por_modelo.append(celular)

  if len(celulares_por_modelo) == 0:
    print(f"Nenhum celular com nome de modelo {nome_modelo} foi encontrado.")
    return
  else:
    for celular in celulares_por_modelo:
        print('\nModelo:', celular['nome'])
        print('Marca:', celular['marca'])
        print('Tamanho da Tela (em \"):', celular['tela'])
        print('Preço: R$', celular['preco'])
        print('Tem câmera frontal?', celular['cam_frontal'])
        print(12*'---')
    
    input("<enter> to continue...\n")
    novo_menu(celulares, celulares_por_modelo)


def listar_celular_por_marca(celulares):

  '''
    Essa função irá primeiro verificar no banco se o nome digitado por ele
    bate completamente ou parcialmente com o nome das marcas registradas no
    banco. Caso sim, a função irá exibir a um ou mais celulares que baterem com
    a pesquisa e executará a função de um submenu, para que opções mais detalhadas
    sejam disponibilizadas para o usuário executar.
  '''

  nome_marca = input("Digite o nome do marca: ")

  celulares_por_marca = []

  for celular in celulares:
    if nome_marca in celular['marca']:
      celulares_por_marca.append(celular)

  if len(celulares_por_marca) == 0:
    print(f"Nenhum celular pertencente à marca {nome_marca} foi encontrado.")
    return
  else:
    for celular in celulares_por_marca:
        print('\nModelo:', celular['nome'])
        print('Marca:', celular['marca'])
        print('Tamanho da Tela (em \"):', celular['tela'])
        print('Preço: R$', celular['preco'])
        print('Tem câmera frontal?', celular['cam_frontal'])
        print(12*'---')

    input("<enter> to continue...\n")
    novo_menu(celulares, celulares_por_marca)


def mostrar_detalhes(celulares_por_parametro):

  '''
    Inicialmente, esta função irá pedir ao usuário que ele digite
    o nome de um celular da qual ele deseja que os detalhes sejam exibidos.
    Caso o celular seja encontrado no banco, suas características são exibidas.
  '''

  nome_celular = input("Digite corretamente o nome do modelo do celular da qual você deseja ver os detalhes: ")

  celular_selecionado = {}

  for celular in celulares_por_parametro:
    if nome_celular == celular['nome']:
      celular_selecionado = celular
    
  if len(celular_selecionado) == 0:
    print(f"O celular com nome {nome_celular} não foi encontrado")
  else:
    print('\nModelo:', celular_selecionado['nome'])
    print('Marca:', celular_selecionado['marca'])
    print('Tamanho da Tela (em \"):', celular_selecionado['tela'])
    print('Preço: R$', celular_selecionado['preco'])
    print('Tem câmera frontal?', celular_selecionado['cam_frontal'])
    print(12*'---')


def remover_celular(celulares, celulares_por_parametro):

  '''
    Inicialmente, esta função irá pedir ao usuário que ele digite
    o nome de um celular da qual ele deseja que seja removido do banco.
    Caso o celular seja encontrado no banco, ele é removido.
  '''

  nome_celular = input("Digite corretamente o nome do modelo da qual você deseja remover: ")

  index_celular_para_remover = -1

  for i in range(len(celulares_por_parametro)):
    if celulares_por_parametro[i]['nome'] == nome_celular:
        index_celular_para_remover = i

  if index_celular_para_remover >= 0:
    for i in range(len(celulares)):
      if celulares[i]['nome'] == celulares_por_parametro[index_celular_para_remover]['nome']:
        celulares.pop(i)

    print("Celular removido com sucesso!")
  else:
    print("Nome digitado incorreto. A operação foi abortada.")
    

def editar_celular(celulares, celulares_por_parametro):

  '''
    Inicialmente, esta função irá pedir ao usuário que ele digite
    o nome de um celular da qual ele deseja que seja editado.
    Caso o celular seja encontrado no banco, ele ira abrir os inputs
    para que o usuário insira os novos dados.
  '''

  nome_celular = input("Digite corretamente o nome do modelo da qual você deseja editar: ")

  index_celular_para_editar = -1

  for i in range(len(celulares_por_parametro)):
    if celulares_por_parametro[i]['nome'] == nome_celular:
      index_celular_para_editar = i

  if index_celular_para_editar >= 0:
    for i in range(len(celulares)):
      if celulares[i]['nome'] == celulares_por_parametro[index_celular_para_editar]['nome']:
        celulares[i]['nome'] = input("Novo nome: ")
        celulares[i]['marca'] = input("Nova marca: ")
        celulares[i]['tela'] = input("Novo tamanho de tela (\"): ")
        celulares[i]['preco'] = definir_preco()
        celulares[i]['cam_frontal'] = temCameraFrontal()
        
        print("Registros alterados com sucesso!\n")


def duplicar_registro(celulares, celulares_por_parametro):

  '''
    Inicialmente, esta função irá pedir ao usuário que ele digite
    o nome de um celular da qual ele deseja que seja duplicado no banco.
    Caso o celular seja encontrado no banco, ele é duplicado.
  '''

  nome_celular = input("Digite corretamente o nome do modelo da qual você deseja duplicar o registro: ")

  celular_duplicado = {}

  for i in range(len(celulares_por_parametro)):
    if celulares_por_parametro[i]['nome'] == nome_celular:
      celular_duplicado = celulares_por_parametro[i]

  if len(celular_duplicado) > 0:
    celulares.append(celular_duplicado)
    print("Registro duplicado com sucesso!")
  else:
    print("Algo deu errado. Operação abortada.")


main()