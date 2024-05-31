senha_cadastrada = "senha123"
email_cadastrado = "paty.fernandes981986@gmail.com"

while True:
    senha_digitada = input("Digite a senha: ")
    email_digitado = input("Digite o email: ")

    if senha_digitada == senha_cadastrada and email_digitado == email_cadastrado:
        print("Login bem-sucedido!")
        break 
    else:
        print("Senha ou email incorretos. Tente novamente.")