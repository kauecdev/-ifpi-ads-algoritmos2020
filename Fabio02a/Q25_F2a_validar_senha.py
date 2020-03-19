def main():
    senha = int(input("Digite sua senha: "))

    verificar_senha(senha)


def verificar_senha(s):
    if s == 1234:
        print("Senha correta, acesso permitido!")
    else: 
        print("Senha incorreta, acesso negado!")


main()