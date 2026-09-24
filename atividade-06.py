senha = int(input("digite a sua senha: "))

while senha != 1234:
    print("Acesso negado!")
    senha = int(input("Digite novamente: "))

print ("Acesso permitio!")